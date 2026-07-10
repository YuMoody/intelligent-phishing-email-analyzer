const form = document.querySelector("#analysis-form");
const fileInput = document.querySelector("#eml_file");
const pastedEmail = document.querySelector("#pasted_email");
const feedback = document.querySelector("#form-feedback");
const submitButton = document.querySelector("#analyze-button");
const submitLabel = submitButton?.querySelector(".button-label");
const demoSampleButtons = document.querySelectorAll(".demo-sample-button");

function showFeedback(message) {
  if (!feedback) return;
  feedback.textContent = message;
  feedback.hidden = false;
}

function clearFeedback() {
  if (!feedback) return;
  feedback.textContent = "";
  feedback.hidden = true;
}

function selectedFileIsValid() {
  const file = fileInput?.files?.[0];
  if (!file) return true;
  return file.name.toLowerCase().endsWith(".eml");
}

function setProcessingState(isProcessing) {
  if (!submitButton || !submitLabel) return;
  submitButton.disabled = isProcessing;
  submitButton.setAttribute("aria-busy", String(isProcessing));
  submitLabel.textContent = isProcessing ? "Analyzing..." : "Analyze Email";
}

function setDemoButtonState(activeButton, isLoading) {
  demoSampleButtons.forEach((button) => {
    button.disabled = isLoading;
    button.setAttribute("aria-busy", String(isLoading && button === activeButton));
  });
}

fileInput?.addEventListener("change", () => {
  if (!selectedFileIsValid()) {
    showFeedback("Invalid file type. Please upload a .eml email file.");
    fileInput.setAttribute("aria-invalid", "true");
    return;
  }

  fileInput.removeAttribute("aria-invalid");
  clearFeedback();
});

pastedEmail?.addEventListener("input", () => {
  pastedEmail.removeAttribute("aria-invalid");
  if (!fileInput?.files?.[0] && pastedEmail.value.trim()) {
    clearFeedback();
  }
});

form?.addEventListener("submit", (event) => {
  const hasFile = Boolean(fileInput?.files?.[0]);
  const hasPastedEmail = Boolean(pastedEmail?.value.trim());

  if (hasFile && !selectedFileIsValid()) {
    event.preventDefault();
    showFeedback("Invalid file type. Please upload a .eml email file.");
    fileInput.setAttribute("aria-invalid", "true");
    fileInput?.focus();
    return;
  }

  if (!hasFile && !hasPastedEmail) {
    event.preventDefault();
    showFeedback("Paste raw email content or upload a .eml file before analyzing.");
    pastedEmail?.setAttribute("aria-invalid", "true");
    pastedEmail?.focus();
    return;
  }

  clearFeedback();
  setProcessingState(true);
});

demoSampleButtons.forEach((button) => {
  button.addEventListener("click", async () => {
    const sampleId = button.dataset.sampleId;
    if (!sampleId || !pastedEmail) return;

    setDemoButtonState(button, true);
    clearFeedback();

    try {
      const response = await fetch(`/demo-samples/${sampleId}`);
      if (!response.ok) {
        throw new Error("Sample could not be loaded.");
      }

      pastedEmail.value = await response.text();
      pastedEmail.removeAttribute("aria-invalid");
      if (fileInput) {
        fileInput.value = "";
        fileInput.removeAttribute("aria-invalid");
      }
      pastedEmail.focus();
      showFeedback("Demo sample loaded. Click Analyze Email to generate the report.");
    } catch {
      showFeedback("Unable to load that demo sample. Please try another scenario.");
    } finally {
      setDemoButtonState(button, false);
    }
  });
});
