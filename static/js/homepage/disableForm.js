$(document).ready(() => {
    $('fieldset').prop('disabled', true)
    $('input[name="subject"], textarea[name="description"], input[name="amount"]').attr('placeholder', 'You have to login first')
})