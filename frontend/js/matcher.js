const matchButton = document.getElementById("matchBtn");
const matchResult = document.getElementById("result");
const matchLoading = document.getElementById("loading");

function escapeMatchHTML(value = "") {
    return String(value).replace(/[&<>"']/g, char => ({
        "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
    })[char]);
}

matchButton.addEventListener("click", async () => {
    const file = document.getElementById("resumeFile").files[0];
    const jobDescription = document.getElementById("jobDescription").value.trim();

    if (!file) return alert("Please select a PDF resume.");
    if (!file.name.toLowerCase().endsWith(".pdf")) return alert("Please upload a PDF file.");
    if (!jobDescription) return alert("Please paste the job description.");

    const formData = new FormData();
    formData.append("file", file);
    formData.append("job_description", jobDescription);

    matchButton.disabled = true;
    matchLoading.style.display = "block";
    matchResult.textContent = "Comparing your resume with the job description...";

    try {
        const response = await fetch("http://127.0.0.1:8000/company_match", {
            method: "POST",
            body: formData
        });
        const data = await response.json();
        if (!response.ok || data.status === "error") throw new Error(data.message || "Resume matching failed.");

        const score = Number(data.score);
        const safeScore = Number.isFinite(score) ? Math.max(0, Math.min(100, score)) : null;
        matchResult.innerHTML = `
            <section class="result-section">
                <h3>Match Score</h3>
                <div class="agent-result-highlight">${safeScore === null ? "—" : `${safeScore}%`}</div>
            </section>
            <section class="result-section">
                <h3>Match Summary</h3>
                <div class="agent-result-text">${escapeMatchHTML(data.reason || "No match explanation was returned.")}</div>
            </section>`;
    } catch (error) {
        matchResult.textContent = error.message || "Unable to match resume. Check that the backend is running.";
        console.error(error);
    } finally {
        matchLoading.style.display = "none";
        matchButton.disabled = false;
    }
});
