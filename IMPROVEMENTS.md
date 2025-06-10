# Code Review Notes

## Bugs and Fixes
- `Neural/rede_neural.py`: `feed_forward` used `self.output_IL_2N` as weights for the second hidden neuron. Fixed to use `self.weights_HL_2N`.

## Potential Improvements
- Normalize player position consistently in `Player` and `Rede_neural` to avoid double scaling.
- Update the `README.md` to reflect Python usage instead of the current Node.js instructions.
- Consider separating game logic and neural network training for easier testing.
- Add automated tests or a simple script to validate basic neural network behaviour.

