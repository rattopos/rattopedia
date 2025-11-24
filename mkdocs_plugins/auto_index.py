"""
MkDocs 플러그인: 블로그 포스트를 자동으로 스캔하여 인덱스 페이지를 생성
"""
import os
import re
import yaml
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options

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
            if len(description_lines) >= 2:
                break
    
    description = ' '.join(description_lines)
    if len(description) > 150:
        description = description[:147] + '...'
    return description

def scan_blog_posts(posts_dir):
    """블로그 포스트 디렉토리를 스캔하여 포스트 정보 수집"""
    posts = []
    posts_path = Path(posts_dir)
    
    if not posts_path.exists():
        return posts
    
    for md_file in posts_path.rglob('*.md'):
        if md_file.name == 'index.md':
            continue
            
        try:
            content = md_file.read_text(encoding='utf-8')
            frontmatter, body = parse_frontmatter(content)
            
            if not frontmatter.get('title'):
                continue
            
            # 상대 경로 계산 (docs 기준)
            # MkDocs는 use_directory_urls: true가 기본이므로 .md 확장자 제거하고 / 추가
            rel_path = md_file.relative_to(posts_path.parent.parent)
            # 절대 경로로 변환 (MkDocs Material의 링크 형식)
            url_path = '/' + str(rel_path).replace('\\', '/').replace('.md', '/')
            
            post = {
                'title': frontmatter.get('title', ''),
                'date': frontmatter.get('date', ''),
                'categories': frontmatter.get('categories', []),
                'tags': frontmatter.get('tags', []),
                'url': url_path,
                'description': get_post_description(body),
            }
            
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
            print(f"Warning: Error processing {md_file}: {e}")
            continue
    
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

def generate_index_markdown(posts):
    """인덱스 페이지 마크다운 생성"""
    categories = defaultdict(list)
    for post in posts:
        if post['categories']:
            for cat in post['categories']:
                categories[cat].append(post)
        else:
            categories['기타'].append(post)
    
    sorted_categories = sorted(categories.items())
    
    lines = [
        '# rattopedia',
        '',
        '수학과 컴퓨터 과학에 관한 학술 블로그입니다.',
        '',
        '---',
        '',
        '## 연구 분야별 글',
        ''
    ]
    
    for category, category_posts in sorted_categories:
        lines.append(f'### {category}')
        lines.append('')
        # HTML 블록 제거 - 순수 마크다운으로 작성
        # CSS로 레이아웃 조정
        lines.append('')
        
        for post in category_posts:
            title = post['title']
            url = post['url']
            description = post['description']
            date = format_date(post['date'])
            tags = format_tags(post['tags'])
            
            # 순수 마크다운으로 작성
            # MkDocs 링크 형식: 상대 경로 사용 (MkDocs가 base path 자동 처리)
            # url에서 앞의 / 제거하여 상대 경로로 변환
            link_path = url[1:] if url.startswith('/') else url
            # 마크다운 링크 형식 사용
            lines.append(f'#### [{title}]({link_path})')
            lines.append('')
            # 설명을 문단으로 작성 - 마크다운이 자동 처리됨
            if description.strip():
                lines.append(description)
                lines.append('')
            if date or tags:
                meta_parts = []
                if date:
                    meta_parts.append(f'Date: {date}')
                if tags:
                    meta_parts.append(f'Tags: {tags}')
                lines.append(f'*{" | ".join(meta_parts)}*')
            lines.append('')
            # 구분선 추가
            lines.append('---')
            lines.append('')
        
        lines.append('')
    
    lines.extend([
        '---',
        '',
        '## 태그',
        '',
        '모든 태그를 보려면 [태그 페이지](/tags/)를 방문하세요.',
        '',
        '## 최근 글',
        ''
    ])
    
    for i, post in enumerate(posts[:10], 1):
        date = format_date(post['date'])
        date_str = f' ({date})' if date else ''
        # 상대 경로로 변환
        link_path = post["url"][1:] if post["url"].startswith('/') else post["url"]
        lines.append(f'{i}. [{post["title"]}]({link_path}){date_str}')
    
    return '\n'.join(lines)

class AutoIndexPlugin(BasePlugin):
    """인덱스 페이지를 자동으로 생성하는 MkDocs 플러그인"""
    
    config_scheme = (
        ('posts_dir', config_options.Type(str, default='blog/posts')),
        ('index_file', config_options.Type(str, default='index.md')),
    )
    
    def on_config(self, config, **kwargs):
        """설정 로드 시 인덱스 페이지 생성"""
        docs_dir = Path(config['docs_dir'])
        posts_dir = docs_dir / self.config['posts_dir']
        index_file = docs_dir / self.config['index_file']
        
        posts = scan_blog_posts(posts_dir)
        index_content = generate_index_markdown(posts)
        
        # 인덱스 파일 업데이트
        index_file.write_text(index_content, encoding='utf-8')
        print(f"✅ 인덱스 페이지가 자동으로 업데이트되었습니다: {index_file}")
        
        return config

