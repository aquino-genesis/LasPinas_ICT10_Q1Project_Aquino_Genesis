document.addEventListener('py:ready', () => {
    const loader = document.getElementById('loadingScreen');
    
    loader.classList.add("flash");

    setTimeout(() => {
        loader.classList.remove("flash");
    }, 100)

    setTimeout(() => {
        loader.classList.add("flash");
    }, 200)

    setTimeout(() => {
        loader.remove();
    }, 300)
});