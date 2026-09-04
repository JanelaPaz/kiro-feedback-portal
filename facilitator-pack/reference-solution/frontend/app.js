const form = document.querySelector('#feedback-form');
const message = document.querySelector('#message');

form.addEventListener('submit', async (event) => {
  event.preventDefault();
  message.textContent = 'Submitting…';

  const payload = {
    workshopTopic: document.querySelector('#workshop-topic').value.trim(),
    rating: Number(document.querySelector('#rating').value),
    comment: document.querySelector('#comment').value.trim(),
  };

  try {
    const response = await fetch(`${window.APP_CONFIG.API_BASE_URL}/feedback`, {
      method: 'POST',
      headers: {'content-type': 'application/json'},
      body: JSON.stringify(payload),
    });
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || 'Submission failed');
    form.reset();
    message.textContent = 'Thanks — your feedback was submitted.';
  } catch (error) {
    message.textContent = error.message;
  }
});
