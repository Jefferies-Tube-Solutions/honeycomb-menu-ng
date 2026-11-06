import CubeElement from './cube-element.js';

// The standalone adapter resolves the same modules and uses the same renderer
// as Hub items and nested menu cubes. Public mode aliases remain optional.
class ControlConsole extends CubeElement {
    static get is() { return 'jts-n-control'; }
}
if (!customElements.get(ControlConsole.is))
    customElements.define(ControlConsole.is, ControlConsole);
window.customCards = window.customCards || [];
if (!window.customCards.some(card=>card.type===ControlConsole.is))
    window.customCards.push({type:ControlConsole.is,name:'Jefferies Navigation Persistent Control',
        description:'Single module using the shared Jefferies Navigation cube engine.'});
export default ControlConsole;
