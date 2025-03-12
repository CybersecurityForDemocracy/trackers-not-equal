class LatexFormatter:
    @staticmethod
    def frac(percentage):
        # FORMAT PERCENTAGE FOR LATEX TABLE
        formatted = f'{percentage:.1f}'
        return f'{formatted}\\%'

    @staticmethod
    def num(number, decimals=None):
        # FORMAT NUMBER FOR LATEX TABLE
        if decimals is not None:
            return f'{number:,.{decimals}f}'
        return f"{number:,}"