"""Plugin functionality for adding optimization backends.

Optimization plugins are managed by a
[`PluginManager`][ropt.plugins.PluginManager] object, which returns classes or
factory functions to create objects that implement one or more optimization
algorithms. These objects must adhere to the
[`Optimizer`][ropt.plugins.optimizer.protocol.Optimizer] protocol. This protocol
allows `ropt` to provide the optimizer with the callback used for evaluating
functions and gradients and allows it to be started from an optimizer step in
the optimization workflow.

To support the implementation of the optimizer classes, the
[`ropt.plugins.optimizer.utils`][ropt.plugins.optimizer.utils] module provides
some utilities.

Optimizers can be added via the plugin manager, by default the
[`SciPyOptimizer`][ropt.plugins.optimizer.scipy.SciPyOptimizer] backend is
installed which provides a number of algorithms from the
[`scipy.optimize`](https://docs.scipy.org/doc/scipy/tutorial/optimize.html)
package.
"""