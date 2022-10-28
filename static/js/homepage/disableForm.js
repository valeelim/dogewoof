$(document).ready(() => {
    $('fieldset').prop('disabled', true)
    $('input[name="subject"], textarea[name="description"]').attr('placeholder', 'You have to login first')
})