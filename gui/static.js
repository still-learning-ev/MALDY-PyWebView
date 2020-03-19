window.addEventListener('pywebviewready', function() {
    var container = document.getElementById('static-status')
    container.innerHTML = '<i>Static Analysis </i> is ready'
})

function showResponse(response) {
    var container = document.getElementById('response-container')

    container.innerText = response.message
    container.style.display = 'block'
}

function start_analysis_static() {
    var retrain = document.getElementById('retrain-model').checked;
    var name_input = document.getElementById('path-to-file').value;
    var btn = document.getElementById('static-bth')
    var retrain_model 
    if (retrain == true){
      retrain_model = 'True'
    }else{
      retrain_model = 'False'
    }
    pywebview.api.start_analysis_static(name_input, retrain_model).then(function(response) {
        showResponse(response)
        btn.onclick = start_analysis_static
        btn.innerText = 'Start'
    })

    showResponse({message: 'Working...'})
    btn.innerText = 'Cancel Analysis'
    btn.onclick = cancel_analysis
}

function cancel_analysis() {
    pywebview.api.cancel_analysis()
}
