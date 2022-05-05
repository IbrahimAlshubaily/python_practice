import jax
import jax.numpy as jnp
from jax import grad, jit
import numpy as np
class regression():
    def __init__(self):
        pass

    def loss_fn_bce(self, params, x, y):
        y_hat = jax.nn.sigmoid(x.dot(params['W']) + params['b'])
        return -(y * jnp.log(y_hat) + (1 - y) * jnp.log(1 - y_hat)).mean()

    def loss_fn_mse(self, params, x, y):
        y_hat = x.dot(params['W']) + params['b']
        return jnp.mean(jnp.square(y - y_hat))
    
    def fit(self, train, test, n_epochs=100, learning_rate = 0.05):
        (x, y), (test_x, test_y) = train, test
        self.is_classification = sum(v==0 or v==1 for v in y) == len(y)
        loss_fn = self.loss_fn_bce if self.is_classification else self.loss_fn_mse
        params = {'W' : jnp.zeros(x.shape[1:]), 'b' : 0.}
        grad_fn = jit(grad(loss_fn))
        loss_curve, test_loss_curve = [], []
        for _ in range(n_epochs):
            grads = grad_fn(params, x,y)
            params = jax.tree_util.tree_map(lambda p, g: p - learning_rate * g, params, grads)
            loss_curve.append(loss_fn(params, x,y).item())
            test_loss_curve.append(loss_fn(params, test_x, test_y).item())
        self.params = params
        return loss_curve, test_loss_curve

    def predict(self, x):
        pred = x.dot(self.params['W']) + self.params['b']
        return jax.nn.sigmoid(pred) if self.is_classification else pred

    def score(self, x, y):
        pred = self.predict(x)
        return 'Accuracy : '+ str(jnp.mean(pred.round() == y).item()) if self.is_classification \
              else 'MSE : '+ str(jnp.mean(jnp.square(y - pred)).item())
    