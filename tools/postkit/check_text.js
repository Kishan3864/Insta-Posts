()=>{
 const out=[];const W=1080,H=1350;
 const leaves=[...document.querySelectorAll('.pg *')].filter(e=>[...e.childNodes].some(n=>n.nodeType==3&&n.textContent.trim()));
 const rectsOf=e=>{const r=document.createRange();const rs=[];e.childNodes.forEach(n=>{if(n.nodeType==3&&n.textContent.trim()){r.selectNodeContents(n);rs.push(...r.getClientRects())}});return rs};
 const L=leaves.map(e=>({e,rs:rectsOf(e)}));
 for(const a of L){for(const r of a.rs){if(r.left<30||r.right>W-30||r.top<15||r.bottom>H-15)out.push('OUT '+a.e.textContent.trim().slice(0,30))}
   const cs=getComputedStyle(a.e);
   if(a.e.scrollWidth>a.e.clientWidth+1&&cs.display!='inline')out.push('HOVERFLOW '+a.e.textContent.trim().slice(0,30));
   if(a.e.scrollHeight>a.e.clientHeight+parseFloat(cs.fontSize)*0.3&&cs.display!='inline')out.push('VOVERFLOW '+a.e.textContent.trim().slice(0,30));
   const fs=parseFloat(cs.fontSize),lh=parseFloat(cs.lineHeight);if(lh&&lh/fs<1.18&&a.rs.length>1)out.push('TIGHT-LH '+a.e.textContent.trim().slice(0,30));
   // text must stay inside its nearest boxed ancestor
   let p=a.e.parentElement;while(p&&p!==document.body){const s=getComputedStyle(p);if(s.backgroundColor!='rgba(0, 0, 0, 0)'||s.backgroundImage!='none'||s.borderTopWidth!='0px')break;p=p.parentElement}
   if(p&&p!==document.body&&!p.classList.contains('pg')){const pr=p.getBoundingClientRect();for(const r of a.rs){if(r.left<pr.left-1||r.right>pr.right+1||r.top<pr.top-1||r.bottom>pr.bottom+1)out.push('ESCAPES-BOX '+a.e.textContent.trim().slice(0,30))}}
 }
 for(let i=0;i<L.length;i++)for(let j=i+1;j<L.length;j++){const A=L[i],B=L[j];if(A.e.contains(B.e)||B.e.contains(A.e))continue;
  for(const r of A.rs)for(const s of B.rs){const w=Math.min(r.right,s.right)-Math.max(r.left,s.left),h=Math.min(r.bottom,s.bottom)-Math.max(r.top,s.top);if(w>1&&h>1)out.push('OVERLAP '+A.e.textContent.trim().slice(0,20)+' / '+B.e.textContent.trim().slice(0,20))}}
 return [...new Set(out)]}