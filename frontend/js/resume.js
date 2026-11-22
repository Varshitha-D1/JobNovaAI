const analyzeButton = document.getElementById("analyzeBtn");

function escapeHTML(value = "") {
    return String(value).replace(/[&<>"']/g, char => ({
        "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
    })[char]);
}

function renderSection(title, content) {
    return `
        <section class="result-section">
            <h3>${escapeHTML(title)}</h3>
            <div class="result-copy">${escapeHTML(content || "No information returned.").trim()}</div>
        </section>`;
}

analyzeButton.addEventListener("click", async () => {
    const file = document.getElementById("resumeFile").files[0];
    const jobDescription = document.getElementById("jobDescription").value.trim();
    const result = document.getElementById("result");
    const loading = document.getElementById("loading");

    if (!file) {
        alert("Please select a PDF resume.");
        return;
    }
    if (!file.name.toLowerCase().endsWith(".pdf")) {
        alert("Please upload a PDF file.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);
    formData.append("job_description", jobDescription);

    analyzeButton.disabled = true;
    loading.style.display = "block";
    result.textContent = "Your resume is being analyzed. Please wait...";

    try {
        const response = await fetch("http://127.0.0.1:8000/analyze_resume", {
            method: "POST",
            body: formData
        });
        const data = await response.json();
        if (!response.ok || data.status === "error") {
            throw new Error(data.message || "Resume analysis failed.");
        }

        result.innerHTML = [
            renderSection("AI Resume Summary", data.summary),
            renderSection("Skill Gap Analysis", data.skill_gap),
            renderSection("Interview Questions", data.questions),
            renderSection("Hire Recommendation", data.hire),
            renderSection("Areas to Improve", data.reject),
            renderSection("Final Verdict", data.judge)
        ].join("");
    } catch (error) {
        result.textContent = error.message || "Unable to analyze resume. Check that the backend is running.";
        console.error(error);
    } finally {
        loading.style.display = "none";
        analyzeButton.disabled = false;
    }
});
