document.addEventListener('py:ready', () => {
    const loader = document.getElementById('loadingScreen');
    
    setTimeout(() => {
        loader.classList.add("flash");
    }, 500); 

    setTimeout(() => {
        loader.classList.remove("flash");
    }, 600)

    setTimeout(() => {
        loader.classList.add("flash");
    }, 700)

    setTimeout(() => {
        loader.remove();
    }, 800)
});