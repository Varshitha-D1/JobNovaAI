const interviewButton = document.getElementById("startInterviewBtn");
const interviewResult = document.getElementById("result");
const interviewLoading = document.getElementById("loading");

function escapeInterviewHTML(value = "") {
    return String(value).replace(/[&<>"']/g, char => ({
        "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
    })[char]);
}

interviewButton.addEventListener("click", async () => {
    const file = document.getElementById("resumeFile").files[0];
    const jobDescription = document.getElementById("jobDescription").value.trim();

    if (!file) return alert("Please select a PDF resume.");
    if (!file.name.toLowerCase().endsWith(".pdf")) return alert("Please upload a PDF file.");

    const formData = new FormData();
    formData.append("file", file);
    formData.append("job_description", jobDescription);

    interviewButton.disabled = true;
    interviewLoading.style.display = "block";
    interviewResult.textContent = "Generating focused interview questions...";

    try {
        const response = await fetch("http://127.0.0.1:8000/analyze_resume", {
            method: "POST",
            body: formData
        });
        const data = await response.json();
        if (!response.ok || data.status === "error") throw new Error(data.message || "Unable to generate interview questions.");

        const questions = String(data.questions || "No interview questions were returned.").trim();
        interviewResult.innerHTML = `<div class="agent-result-text">${escapeInterviewHTML(questions)}</div>`;
    } catch (error) {
        interviewResult.textContent = error.message || "Unable to generate questions. Check that the backend is running.";
        console.error(error);
    } finally {
        interviewLoading.style.display = "none";
        interviewButton.disabled = false;
    }
});
