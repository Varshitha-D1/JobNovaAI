const roadmapButton = document.getElementById("generateRoadmapBtn");
const roadmapResult = document.getElementById("result");
const roadmapLoading = document.getElementById("loading");

function escapeRoadmapHTML(value = "") {
    return String(value).replace(/[&<>"']/g, char => ({
        "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;"
    })[char]);
}

roadmapButton.addEventListener("click", async () => {
    const careerGoal = document.getElementById("careerGoal").value;
    roadmapButton.disabled = true;
    roadmapLoading.style.display = "block";
    roadmapResult.textContent = "Creating your focused skill roadmap...";

    try {
        const response = await fetch("http://127.0.0.1:8000/skill_navigator", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ career_goal: careerGoal })
        });
        const data = await response.json();
        if (!response.ok || data.detail || data.status === "error") {
            throw new Error(data.message || data.detail || "Roadmap generation failed.");
        }
        roadmapResult.innerHTML = `<div class="agent-result-text">${escapeRoadmapHTML(data.roadmap || "No roadmap was returned.").trim()}</div>`;
    } catch (error) {
        roadmapResult.textContent = error.message || "Unable to generate roadmap. Check that the backend is running.";
        console.error(error);
    } finally {
        roadmapLoading.style.display = "none";
        roadmapButton.disabled = false;
    }
});
