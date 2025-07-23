document.addEventListener('DOMContentLoaded', () => {
  const message = document.querySelector('.message');

  // Add click interaction to words
  const words = document.querySelectorAll('.word1, .word2, .word3, .word4');
  words.forEach(word => {
    word.addEventListener('click', () => {
      word.style.transform = 'scale(1.1)';
      setTimeout(() => {
        word.style.transform = 'scale(1)';
      }, 200);
    });
  });

  // Easter egg: Double click to add sparkle effect
  message.addEventListener('dblclick', () => {
    createSparkle(message);
  });

  function createSparkle(element) {
    const sparkle = document.createElement('span');
    sparkle.textContent = '✨';
    sparkle.style.position = 'absolute';
    sparkle.style.left = Math.random() * 100 + '%';
    sparkle.style.top = Math.random() * 100 + '%';
    sparkle.style.animation = 'sparkle 1s forwards';
    element.appendChild(sparkle);

    setTimeout(() => {
      sparkle.remove();
    }, 1000);
  }
});
document.addEventListener('DOMContentLoaded', () => {
  const sec = document.querySelector('.contact-section');
  setTimeout(() => sec.classList.add('visible'), 200);
});
document.querySelectorAll('.form-item input, .form-item textarea').forEach(input => {
  const label = input.parentElement.querySelector('label');

  input.addEventListener('focus', () => {
    label.style.top = '-10px';
    label.style.fontSize = '12px';
    label.style.color = 'black';
  });

  input.addEventListener('blur', () => {
    if (input.value.trim() === '') {
      if (input.tagName.toLowerCase() === 'textarea') {
        label.style.top = '75%';
      } else {
        label.style.top = '50%';
      }
      label.style.fontSize = '16px';
      label.style.color = 'grey';
    }
  });
});

  const scriptURL = 'https://script.google.com/macros/s/AKfycbw5c2V8quLjjSFrVDH-H-_M6wcCoYFF0KZ48ReJbDcEashDjWvkwj0UtGh7RdVFf6H0vA/exec'
  const form = document.forms['submit-to-google-sheet']

  form.addEventListener('submit', e => {
    e.preventDefault()
    fetch(scriptURL, { method: 'POST', body: new FormData(form)})
      .then(response => console.log('Success!', response))
      .catch(error => console.error('Error!', error.message))
  })