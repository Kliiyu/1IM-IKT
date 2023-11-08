function hello() {
    var name = document.getElementById('textbox').value;

    if (name) {
        alert('Hello there, ' + name)
    } else {
        alert('Please name')
    }
}