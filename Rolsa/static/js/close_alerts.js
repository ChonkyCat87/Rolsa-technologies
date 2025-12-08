document.addEventListener("DOMContentLoaded", () => {
    // Get all alerts with dismiss buttons
    const alertList = document.querySelectorAll('.alert');
    alertList.forEach(alert => {
        const btn = alert.querySelector('.btn-close');
        if (btn) {
            btn.addEventListener('click', () => {
                // Use Bootstrap's built-in alert disposal
                const bsAlert = bootstrap.Alert.getOrCreateInstance(alert);
                bsAlert.close();
            });
        }
    });
});