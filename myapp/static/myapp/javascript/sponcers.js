function downloadFile() {
      const filePath = "/media/files/brochure.txt";  // Adjust this path if needed
      const a = document.createElement('a');
      a.href = filePath;
      a.download = 'brochure.txt'; // Optional: rename downloaded file
      document.body.appendChild(a);
      a.click();
      document.body.removeChild(a);
}