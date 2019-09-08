document.addEventListener('DOMContentLoaded', ()=>{
    console.log("__ JS IS RUNNING!")

    let showAnswer = document.querySelector('.answerbtn')
    let newQuestion = document.querySelector('.refreshbtn')
    

    showAnswer.addEventListener('click', ()=>{
        let answer = document.querySelector('#answer')
        answer.classList.toggle('hidden')
    })

    newQuestion.addEventListener('click', ()=>{
        location.reload()
    })

})