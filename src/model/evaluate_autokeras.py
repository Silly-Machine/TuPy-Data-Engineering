def evaluate_model(model, x_test, y_test):
    """
    Evaluate a binary classification model and return various performance metrics.

    Parameters:
    - model: The binary classification model to evaluate.
    - x_test: The input features for testing.
    - y_test: The true labels for testing.

    Returns:
    - accuracy (float): Accuracy of the model.
    - precision (float): Precision of the model.
    - recall (float): Recall of the model.
    - average_f1 (float): Average F1 score of the model.
    - auc (float): Area Under the Receiver Operating Characteristic Curve (AUC-ROC) score.

    Example:
    ```python
    acc, prec, rec, avg_f1, auc = evaluate_model(my_model, test_features, test_labels)
    print(f"Accuracy: {acc}, Precision: {prec}, Recall: {rec}, Average F1: {avg_f1}, AUC: {auc}")
    ```
    """
    logits = model.predict(x_test)

    # Apply sigmoid to get probabilities
    predicted_probabilities = 1 / (1 + np.exp(-logits))

    # Calculate additional metrics
    y_pred_binary = np.round(predicted_probabilities)
    accuracy = accuracy_score(y_test, y_pred_binary)
    precision = precision_score(y_test, y_pred_binary)
    recall = recall_score(y_test, y_pred_binary)

    # Calculate AUC
    auc = roc_auc_score(y_test, predicted_probabilities)

    # Calculate average F1 score
    average_f1 = calculate_average_f1(y_test, y_pred_binary)

    return accuracy, precision, recall, average_f1, auc
