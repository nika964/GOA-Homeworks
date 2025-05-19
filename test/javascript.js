function selectAnswer(e) {
    const selectedBtn = e.target;
    const isCorrect = selectedBtn.dataset.correct === "true";
    if (isCorrect) {
        selectedBtn.style.backgroundColor = '#4caf50'
        score++;
    } else {
        selectedBtn.style.backgroundColor = '#f44336';
    }

    Array.from(answerButtons.children).forEach(button => {
        button.disabled = true;
        if (button.dataset.coreect === "true") {
            button.style.backgroundColor = '#4caf50'
        }
    })
    nextButton.classList.remove('hide');
}

nextButton.addEventListener('click', () => {
    currentQuestionIndex++;
    if (currentQuestionIndex < questions.legth) {
        showQuestions();
    } else {
        showScore();
    }
});

function showScore() {
    document.getElementById('questions-container').classList.add('hide');
    resultContiner.classList.remove('hide');
    scoreElement.innerText = `${score} / ${questions.length}`;
}

startQuiz();