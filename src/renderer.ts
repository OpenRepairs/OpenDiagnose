declare global {
    interface Window {
      electronAPI: {
        setTitle: (title: string) => void;
        startRecovery: () => void;
        endRecovery: () => void;
        batteryData: () => void;
        onBattery: (callback: any) => void;
      };
    }
  }

/**
 * This file will automatically be loaded by webpack and run in the "renderer" context.
 * To learn more about the differences between the "main" and the "renderer" context in
 * Electron, visit:
 *
 * https://electronjs.org/docs/latest/tutorial/process-model
 *
 * By default, Node.js integration in this file is disabled. When enabling Node.js integration
 * in a renderer process, please be aware of potential security implications. You can read
 * more about security risks here:
 *
 * https://electronjs.org/docs/tutorial/security
 *
 * To enable Node.js integration in this file, open up `main.js` and enable the `nodeIntegration`
 * flag:
 *
 * ```
 *  // Create the browser window.
 *  mainWindow = new BrowserWindow({
 *    width: 800,
 *    height: 600,
 *    webPreferences: {
 *      nodeIntegration: true
 *    }
 *  });
 * ```
 */

import './index.css';

console.log('👋 This message is being logged by "renderer.js", included via webpack');

const startButton = document.getElementById('start') as HTMLButtonElement
startButton.addEventListener('click', () => {
  window.electronAPI.startRecovery()
})

const endButton = document.getElementById('end') as HTMLButtonElement
endButton.addEventListener('click', () => {
  window.electronAPI.endRecovery()
})

const batteryButton = document.getElementById('battery') as HTMLButtonElement
batteryButton.addEventListener('click', () => {
  window.electronAPI.batteryData()
})

window.electronAPI.onBattery((value:string) => {
    const json = JSON.parse(value);

    const el = document.getElementById("targetJSON");
    el.innerHTML = JSON.stringify(json, null, 2);
})

function jsonViewer(json:object, collapsible=false) {
    const TEMPLATES: { [key: string]: string } = {
        item: '<div class="json__item"><div class="json__key">%KEY%</div><div class="json__value json__value--%TYPE%">%VALUE%</div></div>',
        itemCollapsible: '<label class="json__item json__item--collapsible"><input type="checkbox" class="json__toggle"/><div class="json__key">%KEY%</div><div class="json__value json__value--type-%TYPE%">%VALUE%</div>%CHILDREN%</label>',
        itemCollapsibleOpen: '<label class="json__item json__item--collapsible"><input type="checkbox" checked class="json__toggle"/><div class="json__key">%KEY%</div><div class="json__value json__value--type-%TYPE%">%VALUE%</div>%CHILDREN%</label>'
    };

    function createItem(key:any, value:any, type:any){
        let element = TEMPLATES.item.replace('%KEY%', key);

        if(type == 'string') {
            element = element.replace('%VALUE%', '"' + value + '"');
        } else {
            element = element.replace('%VALUE%', value);
        }

        element = element.replace('%TYPE%', type);

        return element;
    }

    

    function createCollapsibleItem(key:any, value:any, type:any, children:any){
        let tpl:any = 'itemCollapsible';
        
        if(collapsible) {
            tpl = 'itemCollapsibleOpen';
        }
        
        let element = TEMPLATES[tpl].replace('%KEY%', key);

        element = element.replace('%VALUE%', type);
        element = element.replace('%TYPE%', type);
        element = element.replace('%CHILDREN%', children);

        return element;
    }

    function handleChildren(key:any, value:any, type:any) {
        let html = '';

        for(const item in value) { 
            const _key = item,
                _val = value[item];

            html += handleItem(_key, _val);
        }

        return createCollapsibleItem(key, value, type, html);
    }

    function handleItem(key:any, value:any) {
        const type = typeof value;

        if(typeof value === 'object') {        
            return handleChildren(key, value, type);
        }

        return createItem(key, value, type);
    }

    function parseObject(obj: { [key: string]: any }) {
        let _result = '<div class="json">';

        for(const item in obj) { 
            const key = item,
                value = obj[item];

            _result += handleItem(key, value);
        }

        _result += '</div>';

        return _result;
    }
    
    return parseObject(json);
}