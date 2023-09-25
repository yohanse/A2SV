{
    "integration_methods": [{
        "method_name": "Integration by Substitution (Change of Variable)",
        "method_process": [
                            "Start with the integral of the form ∫f(g(x))g'(x) dx.",
                            "Let u = g(x), then du = g'(x) dx.",
                            "Substitute u for g(x) and du for dx in the integral.",
                            "The integral transforms into ∫f(u) du, which may be easier to solve."
                            ]
    },
        {
        "method_name": "Integration by Parts (Product Rule for Integration)",
        "method_process": [
            "Start with the integral of the form ∫u dv.",
            "Choose parts of the integrand to be 'u' and 'dv'.",
            "Apply the integration by parts formula: ∫u dv = uv - ∫v du.",
            "This transforms the original integral into a combination of simpler integrals."
        ]
    },
        {
        "method_name": "Partial Fraction Decomposition",
        "method_process": [
            "Start with a rational function of the form R(x)/P(x), where R(x) and P(x) are polynomials.",
            "Factor the denominator P(x) into its irreducible factors.",
            "Express the rational function as a sum of partial fractions, where each fraction has a simpler denominator.",
            "Determine the constants for each partial fraction by equating coefficients.",
            "Integrate each partial fraction separately."
        ]
    }
    ],
    "method_usecase": "Three common integration methods include substitution for composite functions, integration by parts for product functions, and partial fraction decomposition for rational functions with numerators of equal or greater degree than denominators.",

    "method_example": [
        "Example:",
        "∫ 2x^3 sin(x^2) dx",

        "Step-by-Step Solution:",

        "1. Integration by Substitution (First Method):",
        "- Choose y = x^2, then dy = 2x dx.",
        "- Rewrite the integral with the new variable:",
        "  ∫ x^2 sin(y) dy",
        "- Since we know y = x^2, the integral simplifies to ∫ y sin(y) dy.",

        "2. Integration (Second Method):",
        "   let u = y and dv = sin(y) dy",
        "   then du = dy and v = -cos(y)",
        "- Using the formula ∫udv = uv - ∫vdu:",
        "   ∫ y * sin(y) dy = -y * cos(y) - ∫ -cos(y) dy",
        "                  = -y * cos(y) + sin(y).",

        "3. Back Substitution:",
        "- We revert to the original variable, y = x^2.",
        "- So, -y * cos(y) + sin(y). translates to -x^2 * cos(x^2) + sin(x^2).",

        "Now, you have the step-by-step solution for the given integral."
    ]
}
