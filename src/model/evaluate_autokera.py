def evaluate_model(model, x_test, y_test):
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