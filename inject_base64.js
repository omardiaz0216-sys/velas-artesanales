const fs = require('fs');
const path = require('path');
const files = ['tofu_1.webp', 'tofu_2.webp', 'mofu_1.webp', 'mofu_2.webp', 'bofu_1.webp', 'bofu_2.webp'];

let jsObj = 'const IMAGES = {\n';
files.forEach(f => {
    const filePath = path.join('assets', f);
    if(fs.existsSync(filePath)) {
        const b64 = fs.readFileSync(filePath).toString('base64');
        jsObj += `    'assets/${f}': 'data:image/webp;base64,${b64}',\n`;
    }
});
jsObj += '};\n';

let html = fs.readFileSync('ads_generator.html', 'utf8');

// Evitar inyectar múltiples veces
if (!html.includes('const IMAGES = {')) {
    html = html.replace('// Init', jsObj + '\n        // Init');
    html = html.replace("document.getElementById('render-bg').src = src;", "document.getElementById('render-bg').src = (typeof IMAGES !== 'undefined' && IMAGES[src]) ? IMAGES[src] : src;");
    fs.writeFileSync('ads_generator.html', html, 'utf8');
    console.log('Injected Base64 successfully.');
} else {
    console.log('Base64 already injected.');
}
