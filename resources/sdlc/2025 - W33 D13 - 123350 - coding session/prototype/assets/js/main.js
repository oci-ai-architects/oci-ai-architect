// main.js - Neuroscience AI Platform Prototype Interactivity

// --- Navigation ---

document.querySelectorAll('nav a').forEach(link => {
  link.addEventListener('click', e => {
    e.preventDefault();
    alert('Navigation is mocked in demo.');
  });
});

// --- Upload Form Validation ---

const form = document.querySelector('form');
if (form) {
  form.addEventListener('submit', function(e) {
    e.preventDefault();
    const mri = document.getElementById('mriFile').files[0];
    const eeg = document.getElementById('eegFile').files[0];
    const notes = document.getElementById('notesFile').files[0];
    if (!mri && !eeg && !notes) {
      alert('Please upload at least one file!');
      return;
    }
    if (mri && !mri.name.endsWith('.dcm')) {
      alert('MRI must be a DICOM .dcm file.');
      return;
    }
    if (eeg && !eeg.name.endsWith('.csv')) {
      alert('EEG must be a .csv file.');
      return;
    }
    if (notes && !notes.name.endsWith('.pdf')) {
      alert('Notes must be a PDF document.');
      return;
    }
    // Simulate upload progress and analysis
    alert('Files validated. Running mock analysis...');
    setTimeout(() => {
      alert('Analysis complete! Risk score ready. (See Results Dashboard)');
    }, 1600);
  });
}

// --- Simulated Knowledge Search ---
const searchBoxes = document.querySelectorAll('input[type=search]');
searchBoxes.forEach(box => {
  box.addEventListener('change', function() {
    alert('Knowledge search is a mockup.\nSample result: "EEG-MRI biomarker review - Science 2022"');
  });
});

// --- Export Demo ---
const exportButton = document.querySelector('section[aria-labelledby=exportSection] button');
if (exportButton) {
  exportButton.addEventListener('click', function(e) {
    e.preventDefault();
    alert('Export is mocked - compliance log updated.');
  });
}

// Add ARIA live feedback for all alerts in real version
