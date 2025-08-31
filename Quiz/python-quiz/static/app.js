'use strict';

const state = {
  quizzes: [],
  currentQuiz: null,
  currentIndex: 0,
  answers: {}, // questionId -> optionIndex
};

const el = (id) => document.getElementById(id);
const viewSelect = el('view-select');
const viewQuiz = el('view-quiz');
const viewResults = el('view-results');
const quizList = el('quiz-list');
const quizTitle = el('quiz-title');
const quizDescription = el('quiz-description');
const questionArea = el('question-area');
const prevBtn = el('prev-question');
const nextBtn = el('next-question');
const backBtn = el('back-button');
const scoreEl = el('score');
const explanationsEl = el('explanations');
const restartBtn = el('restart');

function showView(name) {
  [viewSelect, viewQuiz, viewResults].forEach(v => v.classList.add('hidden'));
  if (name === 'select') viewSelect.classList.remove('hidden');
  if (name === 'quiz') viewQuiz.classList.remove('hidden');
  if (name === 'results') viewResults.classList.remove('hidden');
}

async function loadQuizzes() {
  const res = await fetch('/api/quizzes');
  state.quizzes = await res.json();
  renderQuizList();
}

function renderQuizList() {
  quizList.innerHTML = '';
  state.quizzes.forEach(q => {
    const btn = document.createElement('button');
    btn.className = 'quiz-item';
    btn.textContent = `${q.title} (${q.difficulty})`;
    btn.onclick = () => startQuiz(q.id);
    quizList.appendChild(btn);
  });
}

function startQuiz(quizId) {
  state.currentQuiz = state.quizzes.find(q => q.id === quizId);
  state.currentIndex = 0;
  state.answers = {};
  quizTitle.textContent = state.currentQuiz.title;
  quizDescription.textContent = state.currentQuiz.description;
  showView('quiz');
  renderQuestion();
}

function renderQuestion() {
  const question = state.currentQuiz.questions[state.currentIndex];
  const chosen = state.answers[question.id];
  prevBtn.disabled = state.currentIndex === 0;
  const isLast = state.currentIndex === state.currentQuiz.questions.length - 1;
  nextBtn.textContent = isLast ? 'Finish' : 'Next';

  questionArea.innerHTML = '';
  const qEl = document.createElement('div');
  qEl.className = 'question-card';
  qEl.innerHTML = `
    <div class="q-text">${state.currentIndex + 1}. ${question.question}</div>
    <div class="options"></div>
  `;
  const optionsEl = qEl.querySelector('.options');
  question.options.forEach((opt, idx) => {
    const optBtn = document.createElement('button');
    optBtn.className = 'option' + (chosen === idx ? ' selected' : '');
    optBtn.textContent = opt;
    optBtn.onclick = () => {
      state.answers[question.id] = idx;
      renderQuestion();
    };
    optionsEl.appendChild(optBtn);
  });
  questionArea.appendChild(qEl);
}

function computeResults() {
  const { questions } = state.currentQuiz;
  let correct = 0;
  const details = [];
  questions.forEach(q => {
    const selected = state.answers[q.id];
    const isCorrect = selected === q.correctAnswer;
    if (isCorrect) correct += 1;
    details.push({
      question: q.question,
      selected: typeof selected === 'number' ? q.options[selected] : '—',
      correct: q.options[q.correctAnswer],
      isCorrect,
      explanation: q.explanation,
    });
  });
  return { correct, total: questions.length, details };
}

function renderResults() {
  const { correct, total, details } = computeResults();
  scoreEl.textContent = `You scored ${correct} / ${total}`;
  explanationsEl.innerHTML = '';
  details.forEach(d => {
    const div = document.createElement('div');
    div.className = 'result-item';
    div.innerHTML = `
      <div class="q">${d.question}</div>
      <div class="a ${d.isCorrect ? 'good' : 'bad'}">Your answer: ${d.selected}</div>
      <div class="c">Correct answer: ${d.correct}</div>
      <div class="e">${d.explanation}</div>
    `;
    explanationsEl.appendChild(div);
  });
}

prevBtn.onclick = () => {
  if (state.currentIndex > 0) {
    state.currentIndex -= 1;
    renderQuestion();
  }
};

nextBtn.onclick = () => {
  const isLast = state.currentIndex === state.currentQuiz.questions.length - 1;
  if (isLast) {
    renderResults();
    showView('results');
  } else {
    state.currentIndex += 1;
    renderQuestion();
  }
};

backBtn.onclick = () => {
  showView('select');
};

restartBtn.onclick = () => {
  showView('select');
};

loadQuizzes();


