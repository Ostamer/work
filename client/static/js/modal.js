document.addEventListener('DOMContentLoaded', () => {
    const modal = document.getElementById('custom-modal');
    const openModalButton = document.querySelector('.header-button');
    const closeModalButton = document.getElementById('custom-close-modal');

    // Логирование для отладки
    console.log('openModalButton:', openModalButton);
    console.log('closeModalButton:', closeModalButton);
    console.log('modal:', modal);

    if (openModalButton && closeModalButton && modal) {
        openModalButton.addEventListener('click', () => {
            console.log('Открываю модальное окно');
            modal.classList.remove('hidden');
        });

        closeModalButton.addEventListener('click', () => {
            console.log('Закрываю модальное окно');
            modal.classList.add('hidden');
        });

        window.addEventListener('click', (e) => {
            if (e.target === modal) {
                console.log('Кликнули вне модального окна');
                modal.classList.add('hidden');
            }
        });
    } else {
        console.error("Не удалось найти элементы для модального окна.");
    }
});
