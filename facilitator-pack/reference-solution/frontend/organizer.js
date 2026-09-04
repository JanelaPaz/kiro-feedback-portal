const list = document.querySelector('#feedback-list');
const message = document.querySelector('#message');
const refresh = document.querySelector('#refresh');

function render(items) {
  list.replaceChildren();
  if (!items.length) {
    const empty = document.createElement('p');
    empty.textContent = 'No feedback yet.';
    list.appendChild(empty);
    return;
  }

  for (const item of items) {
    const card = document.createElement('article');
    card.className = 'feedback-item';

    const topic = document.createElement('strong');
    topic.textContent = item.workshopTopic || 'Unknown workshop (legacy)';
    card.appendChild(topic);

    const heading = document.createElement('span');
    heading.textContent = `${item.rating}/5`;
    card.appendChild(heading);

    const time = document.createElement('small');
    time.textContent = item.submittedAt;
    card.appendChild(time);

    const comment = document.createElement('p');
    comment.textContent = item.comment || 'No comment';
    card.appendChild(comment);

    list.appendChild(card);
  }
}

async function loadFeedback() {
  message.textContent = 'Loading…';
  try {
    const response = await fetch(`${window.APP_CONFIG.API_BASE_URL}/feedback`);
    const data = await response.json();
    if (!response.ok) throw new Error(data.error || 'Unable to load feedback');
    render(data.items || []);
    message.textContent = '';
  } catch (error) {
    message.textContent = error.message;
  }
}

refresh.addEventListener('click', loadFeedback);
loadFeedback();
