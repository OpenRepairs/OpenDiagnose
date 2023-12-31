// See the Electron documentation for details on how to use preload scripts:
// https://www.electronjs.org/docs/latest/tutorial/process-model#preload-scripts

import { contextBridge, ipcRenderer } from 'electron';

import { prettyPrintJson } from 'pretty-print-json';

contextBridge.exposeInMainWorld('electronAPI', {
    startRecovery: () => ipcRenderer.send('startRecovery'),
    endRecovery: () => ipcRenderer.send('endRecovery'),
    batteryData: () => ipcRenderer.send('batteryData')
})