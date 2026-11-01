
const button = document.getElementById('startButton');
button.addEventListener('click', function() {
    alert('Plant Transport Simulation started!');

//from aframe and w3schools
const plantEl = document.getElementById('entMacro');
if (plantEl) {
    plantEl.addEventListener('model-loaded', () => {
        const plantMesh = plantEl.getObject3D('mesh');
        if (plantMesh) {
            const Stem_outer = plantMesh.getObjectByName("Stem_outer");
            if (Stem_outer) {
                Stem_outer.visible = false;
                console.log("Success: Stem_outer layer is now hidden.");
            }
        }
    });
}

});
let Stem_outer = Sunflower1.getObjectByName("Stem_outer");
Stem_outer.visible = false;


//from aframe and w3schools 
let activeTranspiration = 1.0;
let activeMassFlow = 1.0;
window.addEventListener('simulationUpdated', (e) => {
    activeTranspiration = e.detail.transpiration;
    activeMassFlow = e.detail.pressure;
    console.log(`[Sync Matrix] Speed updated. Transpiration: ${activeTranspiration}, Phloem: ${activeMassFlow}`);
});
