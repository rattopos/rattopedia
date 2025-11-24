#!/usr/bin/env python3
"""
블로그 포스트를 스캔하여 인덱스 페이지를 자동으로 생성하는 스크립트
"""
import os
import re
import yaml
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def parse_frontmatter(content):
    """마크다운 파일의 frontmatter를 파싱"""
    frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n(.*)$'
    match = re.match(frontmatter_pattern, content, re.DOTALL)
    
    if match:
        frontmatter_str = match.group(1)
        body = match.group(2)
        try:
            frontmatter = yaml.safe_load(frontmatter_str)
            return frontmatter or {}, body
        except yaml.YAMLError:
            return {}, content
    return {}, content

def get_post_description(content):
    """포스트 본문에서 첫 번째 문단을 추출하여 설명으로 사용"""
    # 첫 번째 문단 찾기 (빈 줄 전까지)
    lines = content.split('\n')
    description_lines = []
    for line in lines:
        line = line.strip()
        if not line or line.startswith('#'):
            if description_lines:
                break
            continue
        if line:
            description_lines.append(line)
            if len(description_lines) >= 2:  # 최대 2줄
                break
    
    description = ' '.join(description_lines)
    # 너무 길면 자르기
    if len(description) > 150:
        description = description[:147] + '...'
    return description

def scan_blog_posts(posts_dir):
    """블로그 포스트 디렉토리를 스캔하여 포스트 정보 수집"""
    posts = []
    posts_path = Path(posts_dir)
    
    for md_file in posts_path.rglob('*.md'):
        # index.md는 제외
        if md_file.name == 'index.md':
            continue
            
        try:
            content = md_file.read_text(encoding='utf-8')
            frontmatter, body = parse_frontmatter(content)
            
            if not frontmatter.get('title'):
                continue
            
            # 상대 경로 계산
            rel_path = md_file.relative_to(posts_path.parent.parent)
            url_path = '/' + str(rel_path).replace('\\', '/').replace('.md', '/')
            
            post = {
                'title': frontmatter.get('title', ''),
                'date': frontmatter.get('date', ''),
                'categories': frontmatter.get('categories', []),
                'tags': frontmatter.get('tags', []),
                'url': url_path,
                'description': get_post_description(body),
                'file_path': md_file
            }
            
            # 날짜 파싱
            if post['date']:
                try:
                    if isinstance(post['date'], str):
                        post['date_obj'] = datetime.strptime(post['date'], '%Y-%m-%d')
                    else:
                        post['date_obj'] = post['date']
                except:
                    post['date_obj'] = None
            else:
                post['date_obj'] = None
            
            posts.append(post)
        except Exception as e:
            print(f"Error processing {md_file}: {e}")
            continue
    
    # 날짜순으로 정렬 (최신순)
    posts.sort(key=lambda x: x['date_obj'] or datetime.min, reverse=True)
    return posts

def format_date(date_str):
    """날짜 포맷팅"""
    if not date_str:
        return ''
    try:
        if isinstance(date_str, str):
            date_obj = datetime.strptime(date_str, '%Y-%m-%d')
        else:
            date_obj = date_str
        return date_obj.strftime('%Y-%m-%d')
    except:
        return str(date_str)

def format_tags(tags):
    """태그 포맷팅"""
    if not tags:
        return ''
    return ', '.join(tags)

def generate_index_markdown(posts, output_path):
    """인덱스 페이지 마크다운 생성"""
    # 카테고리별로 그룹화
    categories = defaultdict(list)
    for post in posts:
        if post['categories']:
            for cat in post['categories']:
                categories[cat].append(post)
        else:
            categories['기타'].append(post)
    
    # 카테고리별로 정렬
    sorted_categories = sorted(categories.items())
    
    lines = [
        '# rattopedia',
        '',
        '수학과 컴퓨터 과학에 관한 블로그입니다.',
        '',
        '## 📚 카테고리별 포스트',
        ''
    ]
    
    # 카테고리별 포스트 출력
    for category, category_posts in sorted_categories:
        lines.append(f'### {category}')
        lines.append('')
        
        for post in category_posts:
            title = post['title']
            url = post['url']
            description = post['description']
            date = format_date(post['date'])
            tags = format_tags(post['tags'])
            
            lines.append(f'#### [{title}]({url})')
            lines.append(f'{description}')
            if date or tags:
                meta_parts = []
                if date:
                    meta_parts.append(f'📅 {date}')
                if tags:
                    meta_parts.append(f'🏷️ {tags}')
                lines.append(f'*{" | ".join(meta_parts)}*')
            lines.append('')
        
        lines.append('')
    
    # 태그 섹션
    lines.extend([
        '## 🔖 태그',
        '',
        '모든 태그를 보려면 [태그 페이지](/tags/)를 방문하세요.',
        '',
        '## 📝 최근 포스트',
        ''
    ])
    
    # 최근 포스트 목록 (최대 10개)
    for i, post in enumerate(posts[:10], 1):
        date = format_date(post['date'])
        date_str = f' ({date})' if date else ''
        lines.append(f'{i}. [{post["title"]}]({post["url"]}){date_str}')
    
    # 파일 쓰기
    output_path.write_text('\n'.join(lines), encoding='utf-8')
    print(f"✅ 인덱스 페이지가 생성되었습니다: {output_path}")

def main():
    """메인 함수"""
    # 경로 설정
    base_dir = Path(__file__).parent.parent
    posts_dir = base_dir / 'docs' / 'blog' / 'posts'
    index_path = base_dir / 'docs' / 'index.md'
    
    if not posts_dir.exists():
        print(f"❌ 블로그 포스트 디렉토리를 찾을 수 없습니다: {posts_dir}")
        return
    
    print(f"📂 블로그 포스트 스캔 중: {posts_dir}")
    posts = scan_blog_posts(posts_dir)
    print(f"📝 {len(posts)}개의 포스트를 찾았습니다.")
    
    print(f"📄 인덱스 페이지 생성 중: {index_path}")
    generate_index_markdown(posts, index_path)
    
    print("✨ 완료!")

if __name__ == '__main__':
    main()

