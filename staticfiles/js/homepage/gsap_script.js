gsap.registerPlugin(ScrollTrigger)

gsap.fromTo($('.headline')[0], {
    opacity: 0,
    yPercent: 200
}, {
    opacity: 1,
    yPercent: 0,
    duration: 1.5,
    scrollTrigger: {
        trigger: $('figure'),
        start: '45% center',
    }
})

gsap.fromTo('.navbox-item', {
    opacity: 0,
    xPercent: -50
}, {
    opacity: 1,
    xPercent: 0,
    duration: .3,
    stagger: {
        each: .2
    },
    scrollTrigger: {
        start: 'top bottom',
        trigger: $('.navbox'),
        toggleActions: "restart reverse restart reverse"
    }
})

gsap.fromTo('.c-breed', {
    opacity: 0,
    yPercent: -25
}, {
    opacity: 1,
    yPercent: 0,
    stagger: {
        each: .05
    },
    scrollTrigger: {
        start: 'top bottom',
        trigger: $('#breed-grid'),
        toggleActions: "restart complete none reset"
    }
})