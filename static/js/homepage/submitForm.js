const formatNumber = number => {
    console.log(number)
    number = String(number)
    let formatted_string = ''
    for (let i = 0; i < number.length; i++) {
        if (i % 3 == number.length % 3 && i)
            formatted_string += ','
        formatted_string += number[i]
    }
    return formatted_string
}

$(document).ready(() => {
    $('#contact-form').submit(function(e) {
        e.preventDefault()

        let form = $(this)
        let actionUrl = form.attr('action')

        $.ajax({
            type: 'POST',
            url: actionUrl,
            data: form.serialize(),
            success: () => {
                $('body').append(`
                    <div class="toast-container position-fixed bottom-0 end-0 p-3">
                        <div id="toast" class="toast d-flex" role="alert" aria-live="assertive" aria-atomic="true" style='color: black; font-size: 1.05em'>
                            <div class="toast-header" style='background-color: white'>
                                <img src="/static/images/homepage/success.svg" style='width: 30px'>
                            </div>
                            <div class="toast-body d-flex flex-column ps-0">
                                <strong>Success</strong>
                                <div>
                                    Message successfully sent!
                                </div>
                            </div>
                        </div>
                    </div>
                `)
                $('#toast').toast('show')
                form.trigger('reset')
            }
        })
    })

    $('#donation-form').submit(function(e) {
        e.preventDefault()

        let form = $(this)
        let actionUrl = form.attr('action')
        console.log($('#total-donation h1 strong')[0].textContent)

        $.ajax({
            type: 'POST',
            url: actionUrl,
            data: form.serialize(),
            success: resp => {
                let e = '#total-donation h1 strong'
                let value = parseInt($(e)[0].textContent.replaceAll(',', '')) + resp.donated_amount
                $(e).text(formatNumber(value))
                form.trigger('reset')
            }
        })
    })
})