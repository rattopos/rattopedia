window.MathJax = {
  loader: {load: ['[tex]/mathtools','[tex]/physics']},
  tex: {
    inlineMath: [["\\(", "\\)"], ["$", "$"]],
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],
    processEscapes: true,
    processEnvironments: true,
    packages: {'[+]': ['mathtools','physics']},
    autoload: {
      color: [],
      colorv2: ['color']
    },
    macros: {
      RR: "{\\mathbb{R}}",
      NN: "{\\mathbb{N}}",
      ZZ: "{\\mathbb{Z}}",
      QQ: "{\\mathbb{Q}}",
      CC: "{\\mathbb{C}}",
      FF: "{\\mathbb{F}}"
    }
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  },
  startup: {
    ready: () => {
      MathJax.startup.defaultReady();
      MathJax.startup.promise.then(() => {
        console.log('MathJax is ready');
      });
    }
  }
};

// MkDocs Material의 document$ 이벤트 구독 (디바운싱 추가)
if (typeof document$ !== 'undefined') {
  let mathjaxTimeout = null;
  let isRendering = false;
  
  document$.subscribe(() => { 
    // 이미 렌더링 중이면 무시
    if (isRendering) {
      return;
    }
    
    // 디바운싱: 300ms 내에 여러 이벤트가 발생해도 한 번만 실행
    if (mathjaxTimeout) {
      clearTimeout(mathjaxTimeout);
    }
    
    mathjaxTimeout = setTimeout(() => {
      if (window.MathJax && window.MathJax.typesetPromise && !isRendering) {
        isRendering = true;
        MathJax.startup.output.clearCache();
        MathJax.typesetClear();
        MathJax.texReset();
        MathJax.typesetPromise()
          .then(() => {
            isRendering = false;
          })
          .catch((err) => {
            console.error('MathJax rendering error:', err);
            isRendering = false;
          });
      }
    }, 300);
  });
}

// 페이지 로드 시에도 MathJax 실행 (한 번만)
let initialRenderDone = false;
document.addEventListener('DOMContentLoaded', function() {
  if (!initialRenderDone && window.MathJax && window.MathJax.typesetPromise) {
    initialRenderDone = true;
    MathJax.typesetPromise().catch((err) => {
      console.error('MathJax initial rendering error:', err);
    });
  }
});

