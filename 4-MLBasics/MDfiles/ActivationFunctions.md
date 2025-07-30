Activation functions are crucial components in neural networks, introducing non-linearity and enabling the model to learn complex patterns. Here’s a list of common activation functions used in **hidden layers** and **fully connected (dense) layers**:

### **1. Common Activation Functions for Hidden Layers**  
These are the most widely used activation functions in hidden/fully connected layers:

#### **A. Sigmoid (Logistic)**
   - Formula: \( \sigma(x) = \frac{1}{1 + e^{-x}} \)
   - Output Range: (0, 1)
   - **Pros**: Smooth gradient, good for binary classification in output layers.
   - **Cons**: Suffers from vanishing gradients, not zero-centered.

#### **B. Hyperbolic Tangent (Tanh)**
   - Formula: \( \tanh(x) = \frac{e^x - e^{-x}}{e^x + e^{-x}} \)
   - Output Range: (-1, 1)
   - **Pros**: Zero-centered, stronger gradients than sigmoid.
   - **Cons**: Still suffers from vanishing gradients for deep networks.

#### **C. Rectified Linear Unit (ReLU)**
   - Formula: \( \text{ReLU}(x) = \max(0, x) \)
   - Output Range: [0, ∞)
   - **Pros**: Computationally efficient, avoids vanishing gradients (for positive inputs).
   - **Cons**: "Dying ReLU" problem (neurons can get stuck at zero).

#### **D. Leaky ReLU**
   - Formula: \( \text{LeakyReLU}(x) = \begin{cases} x & \text{if } x > 0 \\ \alpha x & \text{otherwise} \end{cases} \) (where \( \alpha \) is a small slope, e.g., 0.01)
   - **Pros**: Fixes the "dying ReLU" problem by allowing small negative outputs.
   - **Cons**: Requires tuning \( \alpha \) in some cases.

#### **E. Parametric ReLU (PReLU)**
   - Similar to Leaky ReLU, but \( \alpha \) is learned during training.
   - **Pros**: Adapts the negative slope for better performance.
   - **Cons**: Slightly more computationally expensive.

#### **F. Exponential Linear Unit (ELU)**
   - Formula: \( \text{ELU}(x) = \begin{cases} x & \text{if } x > 0 \\ \alpha (e^x - 1) & \text{otherwise} \end{cases} \)
   - **Pros**: Smooth gradient for negative inputs, avoids dying ReLU.
   - **Cons**: Computationally more expensive than ReLU.

#### **G. Swish**
   - Formula: \( \text{Swish}(x) = x \cdot \sigma(\beta x) \) (where \( \sigma \) is the sigmoid function)
   - **Pros**: Smooth, non-monotonic, often outperforms ReLU in deep networks.
   - **Cons**: Slightly more computationally expensive.

#### **H. Gaussian Error Linear Unit (GELU)**
   - Formula: \( \text{GELU}(x) = x \cdot \Phi(x) \) (where \( \Phi(x) \) is the CDF of Gaussian distribution)
   - **Pros**: Used in transformers (e.g., BERT, GPT), performs well in deep networks.
   - **Cons**: More complex computation.

#### **I. Scaled Exponential Linear Unit (SELU)**
   - A self-normalizing variant of ELU when used with proper weight initialization (e.g., LeCun normal).
   - **Pros**: Enables self-normalizing networks (avoids batch normalization).
   - **Cons**: Requires specific initialization and architecture.

### **2. Activation Functions Typically Used in Output Layers**
While the above functions are for hidden layers, output layers often use:
- **Regression (Linear Output)**: No activation (or linear activation).
- **Binary Classification**: Sigmoid.
- **Multiclass Classification**: Softmax.

### **Summary of Best Practices**
| **Use Case**          | **Recommended Activation**  |
|-----------------------|-----------------------------|
| **Hidden Layers (General)** | ReLU, Leaky ReLU, Swish, GELU |
| **Deep Networks**      | SELU (with proper init), GELU |
| **Avoid Vanishing Gradients** | Leaky ReLU, ELU, Swish |
| **Transformers (e.g., BERT, GPT)** | GELU |
