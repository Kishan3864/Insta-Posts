// usage: node peep.js '<json props>'  -> prints svg
const React=require('react');const {renderToStaticMarkup}=require('react-dom/server');
const Peep=require('react-peeps').default;
const p=JSON.parse(process.argv[2]);
const svg=renderToStaticMarkup(React.createElement(Peep,{style:{width:'100%',height:'100%'},...p}));
process.stdout.write(svg);
