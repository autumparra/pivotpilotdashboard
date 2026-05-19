const API_URL = 'http://localhost:3000/api/dashboard';

async function loadLiveDashboard() {
  try {
    const response = await fetch(API_URL);
    if (!response.ok) throw new Error('Network response was not ok');
    
    const data = await response.json();

    // 1. Update the Streak Footer
    const streakElement = document.querySelector('em:last-of-type'); 
    if (streakElement) {
      streakElement.textContent = `Current streak: ${data.streak} days 🔥`;
    }

    // 2. Update Today's Brief Section
    // (Targeting the section under ## 🔥 Today's Brief)
    const briefSection = document.querySelector('h2:nth-of-type(1)').nextElementSibling;
    if (briefSection) {
      briefSection.innerHTML = data.brief.map(task => {
        const icon = task.completed ? '✅' : '📅';
        return `<span>${icon} ${task.text} </span>`;
      }).join('');
    }

    // 3. Update Job Pipeline Section
    const pipelineList = document.querySelector('ul'); // Targets your current job bullet points
    if (pipelineList) {
      pipelineList.innerHTML = data.pipeline.map(job => `
        <li>
          *${job.title}* ${job.company} • ${job.location} *<strong>${job.status}</strong>*
        </li>
      `).join('');
    }

    // 4. Update Email Summary Section
    const emailSection = document.querySelector('h2:nth-of-type(3)').nextElementSibling;
    if (emailSection) {
      emailSection.innerHTML = `
        <p>🔥 ${data.emailSummary.recruiterMessages} new recruiter messages</p>
        <p>📅 ${data.emailSummary.interviewInvites} upcoming interview invite</p>
        <p>🔕 ${data.emailSummary.filteredLowPriority} low-priority emails filtered</p>
      `;
    }

  } catch (error) {
    console.error("Failed to fetch live dashboard data:", error);
  }
}

// Fire it up when the page loads
document.addEventListener('DOMContentLoaded', loadLiveDashboard);
