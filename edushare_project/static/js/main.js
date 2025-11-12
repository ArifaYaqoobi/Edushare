document.addEventListener('DOMContentLoaded', function(){
  const searchBtn = document.getElementById('search-btn');
  if (!searchBtn) return;

  async function doSearch(){
    const q = document.getElementById('search-input').value;
    const subject = document.getElementById('subject-filter').value;
    const grade = document.getElementById('grade-filter').value;
    const params = new URLSearchParams();
    if (q) params.append('q', q);
    if (subject) params.append('subject', subject);
    if (grade) params.append('grade', grade);
    const resp = await fetch('/api/search/?' + params.toString());
    const data = await resp.json();
    const results = document.getElementById('results');
    results.innerHTML = '';
    if (data.results.length === 0) {
      results.innerHTML = '<p class="text-muted">No resources found.</p>';
      return;
    }
    for (const r of data.results) {
      const div = document.createElement('div');
      div.className = 'col-12 col-sm-6';
      div.innerHTML = `
        <div class="card h-100">
          <div class="card-body">
            <h5 class="card-title"><a href="/resource/${r.id}/">${r.title}</a></h5>
            <p class="card-text small text-muted">${r.subject} • ${r.grade}</p>
            <p class="card-text small text-muted">by ${r.owner} • ${r.created_at}</p>
          </div>
        </div>
      `;
      results.appendChild(div);
    }
  }

  searchBtn.addEventListener('click', doSearch);
  document.getElementById('search-input').addEventListener('keydown', function(e){
    if (e.key === 'Enter') { e.preventDefault(); doSearch(); }
  });
});
