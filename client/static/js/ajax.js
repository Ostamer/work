$(document).ready(function () {
    const phoneField = document.querySelector('.phone_field');

    // Инициализация IMask для ввода телефона
    const phoneMask = IMask(phoneField, {
        mask: '+{7} (000) 000-00-00'
    });

    // Очищаем некорректный ввод (например, при вставке текста)
    phoneField.addEventListener('input', function () {
        let currentNumber = phoneField.value;

        // Удаляем все, кроме разрешенных символов
        currentNumber = currentNumber.replace(/[^\d\+\-\(\)\s]/g, '');
        phoneField.value = currentNumber;
    });

    $('.input_container').on('submit', function (e) {
        e.preventDefault();

        const name = $('.input_field').val().trim();
        const phoneNumber = phoneField.value;

        if (!name) {
            toastr.warning('Введите ваше имя', 'Внимание');
            return;
        }

        // Проверяем, что телефон введен корректно (в данном случае проверяется длина)
        const isValidPhone = phoneNumber.replace(/\D/g, '').length === 11; // 11 цифр для России (+7)

        if (!isValidPhone) {
            toastr.warning('Введите корректный номер телефона', 'Внимание');
            return;
        }

        $.ajax({
            type: 'POST',
            url: ajaxSubmitClientUrl,
            data: {
                name: name,
                phone_number: phoneNumber,
                csrfmiddlewaretoken: csrfToken
            },
            success: function (response) {
                if (response.success) {
                    toastr.success(response.message, 'Успех');
                    $('.input_field').val('');
                    phoneField.value = '';
                    phoneMask.updateValue();
                } else {
                    toastr.warning(response.message, 'Внимание');
                }
            },
            error: function (xhr) {
                if (xhr.responseJSON && xhr.responseJSON.errors) {
                    const errors = xhr.responseJSON.errors;
                    let errorMsg = '';
                    for (const field in errors) {
                        errorMsg += `${field}: ${errors[field].join(', ')}<br>`;
                    }
                    toastr.error('Ошибки:<br>' + errorMsg, 'Ошибка');
                } else {
                    toastr.error('Произошла ошибка при отправке данных.', 'Ошибка');
                }
            }
        });
    });

    toastr.options = {
        closeButton: true,
        debug: false,
        newestOnTop: true,
        progressBar: true,
        positionClass: 'toast-top-right',
        preventDuplicates: true,
        showDuration: '300',
        hideDuration: '1000',
        timeOut: '5000',
        extendedTimeOut: '1000',
        showEasing: 'swing',
        hideEasing: 'linear',
        showMethod: 'fadeIn',
        hideMethod: 'fadeOut'
    };
});
