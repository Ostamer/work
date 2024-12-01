const changeStage = (currentStage, nextStage) => {
    const currentStageElem = document.querySelector(`.quiz .quiz-container .stage${currentStage}`);
    const nextStageElem = document.querySelector(`.quiz .quiz-container .stage${nextStage}`);

    currentStageElem.classList.remove('show');
    nextStageElem.classList.add('show');
}

const slider = document.getElementById('slider');
const sliderValue = document.getElementById('slider-value');

const updateInputRange = () => {
    sliderValue.innerHTML = Number(slider.value).toLocaleString('de-DE');

    const percentage = (slider.value - slider.min) / (slider.max - slider.min) * 97;

    sliderValue.style.left = `calc(${percentage}% - ${sliderValue.offsetWidth / 2 - 70}px)`;

    slider.style.background = `linear-gradient(to right, #FD554B ${percentage}%, white ${percentage}%)`;
}

slider.addEventListener('input', updateInputRange);

updateInputRange();

$('.send_form').submit((e) => {
    e.preventDefault();

    const data = {
        name: document.querySelector('.quiz .quiz-container form .quiz_name').value,
        phoneNumber: document.querySelector('.quiz .quiz-container form .quiz_phone').value,
        price: document.querySelector('.quiz .quiz-container form .quiz_price').value,
        marks: document.querySelector('.quiz .quiz-container form .quiz_marks').value,
        description: document.querySelector('.quiz .quiz-container form .quiz_description').value,
        csrfmiddlewaretoken: new FormData(e.target).get('csrfmiddlewaretoken')
    }

    $.ajax({
        url: `/quiz/`,
        type: 'POST',
        data: data,
        success: function (data) {
            changeStage(4, 5)
        },
        error: function (xhr, status, error) {
            console.error('Ошибка AJAX:', error);
        }
    });
});

// Просто отображаем квиз сразу
document.addEventListener("DOMContentLoaded", () => {
    // Убедимся, что квиз сразу отображается как обычный блок
    document.querySelector('.quiz').classList.add('show');
});
