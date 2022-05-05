import jax
import jax.numpy as jnp
from jax import grad, jit

class linear_regression():
    def __init__(self):
        pass


    def fit(self, train, test, n_epochs=100, learning_rate = 1e-4):
        (x, y), (test_x, test_y) = train, test
        params = {'W' : jnp.zeros(x.shape[1:]), 'b' : 0.}
        loss_fn = lambda params, x,y: jnp.mean(jnp.square((x.dot(params['W']) + params['b']) - y))
        grad_fn = jit(grad(loss_fn))
        loss_curve, test_loss_curve = [], []
        for _ in range(n_epochs):
            grads = grad_fn(params, x,y)
            params = jax.tree_util.tree_map(lambda p, g: p - 0.05 * g, params, grads)
            loss_curve.append(loss_fn(params, x,y))
            test_loss_curve.append(loss_fn(params, test_x, test_y))
        
        self.params = params
        return loss_curve, test_loss_curve


    def predict(self, X):
        return X.dot(self.params['W']) + self.params['b']