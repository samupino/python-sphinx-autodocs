"""Module A docstring summary.

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Pellentesque
commodo nisi varius tellus feugiat, eu mattis massa congue. Mauris
lacinia turpis at tellus maximus congue. In in viverra risus. Proin
pulvinar feugiat malesuada. Cras et viverra enim, nec consequat metus.
Suspendisse at est tristique, laoreet urna id, tristique leo. In hac
habitasse platea dictumst. Nulla facilisi. Nullam convallis nunc mauris,
vel egestas quam blandit nec. Quisque nec lorem ac neque placerat
semper. Mauris lobortis non nulla id volutpat. Suspendisse imperdiet
commodo est a placerat. Fusce faucibus laoreet augue, quis interdum
ligula rhoncus cursus. Nam sodales vulputate turpis in varius.
"""


class ClassA:
    """ClassA docstring summary.

    Vivamus nec metus vulputate, ullamcorper diam at, accumsan nunc.
    Fusce vitae ullamcorper nunc, molestie viverra mi. Aenean pharetra
    nulla id accumsan aliquet. Phasellus vulputate augue ut lorem
    laoreet, eget congue diam laoreet.
    """

    def return_zero(self, a: int, b: str) -> int:
        """sample_method docstring summary.

        Return zero whatever parameters (lol).

        Parameters
        ----------
        a : int
            An integer parameter.
        b : str
            A string parameter.

        Return
        ------
        int
            The result of a complex computation.
        """

        return 0


class ClassWithoutDocstrings:
    pass


class _NonPublicClass:
    """This is a non pubic class, since it starts with '_'.

    Vivamus nec metus vulputate, ullamcorper diam at, accumsan nunc.
    Fusce vitae ullamcorper nunc, molestie viverra mi. Aenean pharetra
    nulla id accumsan aliquet. Phasellus vulputate augue ut lorem
    laoreet, eget congue diam laoreet.
    """
    pass


class _NonPublicClassWithoutDocstring:
    pass
