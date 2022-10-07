---
authors: [ Geoffrey Hunter ]
categories: [ Electronics, Circuit Design ]
date: 2013-01-03
description: A tutorial on analogue electronic filters, including low-pass/high-pass 1st order RC, LC and RLC filters and 2nd order RC, Sallen-Key filter topologies.
draft: false
lastmod: 2022-09-20
tags: [ electronics, circuit design, filters, passive filters, active filters, RC, low-pass, high-pass, LC, bode plot, frequency response, Sallen-Key, voltage-controlled voltage source, VCVS, cutoff frequency, corner frequency, break frequency, elliptic filters, Cauer filter, Zolotarev filter ]
title: Analogue Filters
type: page
---

## Overview

Related pages:

* [Sallen-Key Filters]()

### Passive vs. Active

Even in the pass-band, passive filters almost always increase the impedance of the signal, post filter. For a trace on a circuit board, this actually makes the post-filter trace more susceptible to picking up external noise. For this reason, when using a passive filter to filter out induced noise of a sensitive trace, always place a passive filter as close as possible to the receiving end of the signal (e.g. as close as possible to an ADC pin on a microcontroller).

Low-pass filters have an additional advantage when used on the analogue outputs from microcontrollers. If the DAC does not work properly for some reason (assuming you are using a DAC), you can sometimes implement the desired behaviour by using PWM instead. With the cut-off frequency set correctly, the PWM signal will be filtered so that a DC voltage proportional to the duty cycle remains, which is what you wished to implement with the DAC in the first place.

Active filters are electronic waveform filters which require their own power source (such as any filter powered with an [op-amp](/electronics/components/op-amps)), as opposed to passive filters (such as RC filters) which do not require an external power source. Active filters allow higher roll-of and better transfer characteristics than passive filters, but require more componentry and consume power.

### Filter Topologies vs. Tunings

* _Filter types_ describe the purpose of the filter. Filter types include low-pass, high-pass, band-pass, notch (band reject), and all-pass.
* _Filter topologies_ define the what components go where. Filter topologies include 
* _Filter tunings_ define the values of the components in a particular topology. Filter tunings include Butterworth, Chebyshev and Bessel.

### Filter Parameters

#### Cutoff Frequency (fc)

The _cutoff frequency_ (a.k.a. _corner frequency_ or _break frequency_) is the frequency which marks the **transition from a pass band to a stop band**. It marks the frequency at which the energy (whether it be voltage, current or both) stops being passed through and begins being blocked. For any real filter, there is a transition from the passband to the stopband, as so the cutoff frequency is usually defined at the "-3dB" point --- the point at which the **signal degrades to -3dB (half power) of the nominal passband value**.

The symbol `\(f_c\)` is usually used to represent the cutoff frequency. Sometimes you may see `\(f_{-3dB}\)` instead.

#### Gain Factor (K)

At frequencies `\(f << f_c\)`, the circuit multiplies the input signal by gain factor `K`.

#### Component Spread

_Component spread_ is a measure of ratio between the highest and lowest valued components required to construct a filter. Low component spread is a good property for a filter to have, as it aids manufacturability.

#### Filter Optimizations

_Filter optimizations_ maximize a certain characteristic of a filter topology, such as maximum pass-band flatness or steepest roll-off. Butterworth, Chebyshev and Bessel are examples of filter optimizations.

## 1st Order Filters

### First-Order Low-Pass RC Filter

#### Schematic

The below schematic shows a first-order low-pass RC filter consisting of a single series resistor and then a single capacitor to ground.

{{% figure src="low-pass-rc/low-pass-rc-filter-schematic.svg" width="500px" caption="Schematic of a simple low-pass RC filter." %}}

The low-pass RC filter lets through low frequencies but dampens high frequencies.

#### How To Choose R And C

The cut-off frequency is determined by **both the value of the resistor and the value of the capacitor**, and is equal to:

<p>\begin{align}
f_{c} = \frac{1}{2\pi RC}
\end{align}</p>

<p class="centered">
where:</br>
\(R\) is the resistance, in Ohms</br>
\(C\) is the capacitance, in Farads</br>
\(f_c\) is the cut-off frequency, in Hertz</br>
</p>

As usual, the choice of `\(R\)` and `\(C\)` is a design decision which involves trade-offs. In terms of choosing `\(R\)`:

* A resistance which is too small could draw too much current, either presenting too much load to the input, or overheating. It also could mean that the capacitor has to be very large and/or expensive to get the desired cut-off frequency.
* A resistance which is too large increases the output impedance of the filter, resulting in distortions if too much load is applied to `\(V_{out}\)`. It also increases the noise susceptibility of the circuit.

Typically, a resistance between `\(1k\Omega\)` and `\(100k\Omega\)` is used. Then the capacitance is chosen to give the desired cut-off frequency.

#### Frequency Response

To plot the frequency response, we first need to find the transfer function for the low-pass RC filter. We can use the voltage divider rule to write `\(v_{out}\)` as a function of `\(v_{in}\)`:

<p>\begin{align}
\frac{V_{out}}{V_{in}} = \frac{X_C}{X_C + R}
\end{align}</p>

<p class="centered">
where:</br>
\(v_{in}\) is the magnitude of the input signal at frequency \(f\), in Volts</br>
\(X_C\) is the impedance of the capacitor at frequency \(f\), in Ohms</br>
\(R\) is the resistance of the resistor, in Ohms</br>
</p>

Recall that we can write `\(X_C\)` in the Laplace domain as `\(X_C = \frac{1}{sC}\)`. Also, `\(\frac{v_{out}}{v_{in}}\)` is just our transfer function `\(H(s)\)`:

<p>\begin{align}
H(s) = \frac{\frac{1}{sC}}{\frac{1}{sC} + R}
\end{align}</p>

Multiply top and bottom by `\(\frac{1}{sC}\)` to clean things up:

<p>\begin{align}
H(s) = \frac{1}{1 + sRC}
\end{align}</p>

Now replace `\(s\)` with `\(j\omega\)` so we can then take the magnitude:

<p>\begin{align}
H(j\omega) = \frac{1}{1 + j\omega RC}
\end{align}</p>

Now take the magnitude (for more info on why and how to do this, see the [What Are Transfer Functions, Poles, And Zeroes? page](/electronics/circuit-design/what-are-transfer-functions-poles-and-zeroes/)):

<p>\begin{align}
\label{eq:abc}
| H(j\omega) | &= \left| \frac{1}{1 + j\omega RC} \right| \nonumber \\
         &= \frac{1}{\sqrt{(1 + j\omega RC)(1 - j\omega RC)}} \nonumber \\
         &= \frac{1}{\sqrt{1 - (j\omega RC)^2}} \nonumber \\
         &= \frac{1}{\sqrt{1 - (-1)(\omega RC)^2}} \nonumber \\
\label{eq:mag-response-lp-rc-filter}
         &= \frac{1}{\sqrt{1 + (\omega RC)^2}} \\
\end{align}</p>

And let's find the phase response:

<p>\begin{align}
\angle H(j\omega) &= Arg\left(H(j\omega)\right) \nonumber \\
                  &= Arg\left(\frac{1}{1 + j\omega RC}\right) \nonumber \\
                  &= Arg(1) - Arg(1 + j\omega RC) \nonumber \\
                  &= 0 - arctan\left(\frac{j\omega RC}{1}\right) \nonumber \\
\label{eq:phase-response-lp-rc-filter}
                  &= -arctan\left(j\omega RC\right) \\
\end{align}</p>

This shows us that an RC filter "delays" signals as they pass through. The higher the frequency, the greater the delay.

The following plot shows the frequency response (also known as a _bode plot_) of a low-pass filter, with values `\(R = 1k\Omega\)` and `\(C = 1\mu F\)`. Magnitude is plotted in blue and phase in green.

{{% figure src="rc-low-pass-filter-frequency-response.png" width="700px" caption="The frequency response (magnitude and phase) of a low-pass RC filter." %}}

The cut-off frequency (also called the _break frequency_ or _turnover frequency_[^bib-wikipedia-low-pass-filter]), `\(f_c\)` is not the frequency at which all higher frequencies are stopped (remember, this is an ideal filter, but in real-life they always let through some fraction of the higher-frequencies). Instead, it is the frequency at where:

<p>\begin{align}
V_{out} = \frac{1}{\sqrt{2}} V_{in} = 0.707*V_{in}
\end{align}</p>

The choice of resistor and capacitor above gives a cut-off frequency of `\(f_c = 159Hz\)`.

Low-pass RC filters are typically used for applications up to 100kHz, above 100kHz RLC filters are used[^bib-elec-tutorial-filters].

#### Time Constant

The time constant `\(\tau\)` of a low-pass RC filter is[^bib-wikipedia-low-pass-filter]:

<p>\begin{align}
\tau = RC
\end{align}</p>

#### Typical Uses

The low-pass RC filter is one (if not) the most commonly used filters on circuit board designs. Its popularity results from it's simplicity (two passive components), low cost (one resistor, one capacitor), small size, and it's myriad of uses.

Due to the presence of the resistor, it is a lossy filter, and therefore not suited for high-power applications (use a low-pass LC filter instead).

The low-pass RC filter can be used to provide filtering on analogue inputs to a microcontroller before being sampled by the ADC. One example could be to filter the output of an analogue temperature sensor. Note that is **normally advantageous to place the filter as close as possible to the microcontroller**, rather than close to the sensor producing the voltage. This is because the series resistor of the RC filter increases the source impedance of the analogue signal, **making the PCB track less immune to noise once it passes through the resistor**.

Another way to reduce the reduction in noise immunity due to the resistor in the RC low-pass filter is **to make the capacitor as large as practically possible** (for a particular cut-off frequency). Both the resistance and the capacitance influence the cut-off frequency. If you increase the capacitance by 10x, and reduce the resistance by 10x, you get the same cut-off frequency, but far better noise immunity since the source impedance is not altered as much.

**Another consideration is the effect of the increase in source impedance (due to the resistor in the RC filter) when connecting the output to something like a [microcontroller ADC](/electronics/circuit-design/adcs)).** The input impedance of an non-buffered ADC pin on a microcontroller is usually somewhere between `\(20-500k\Omega\)` (note that this is usually variable, and can change with sampling rate). This will form a resistor divider with the RC filter resistance, increasing the ADC measurement error. As a general rule, **you want the RC filter resistance to be much lower than the ADC input impedance**.

<p>\begin{align}
R_{RC filter} << R_{ADC}
\end{align}</p>

**A RC filter resistance which is at least 50x lower than the ADC input impedance is acceptable in most cases.** For a standard ADC input impedance of `\(50k\Omega\)`, this means that the resistor in the RC filter should be no more than `\(1k\Omega\)`.

#### Transient Response

The equation for the voltage across the capacitor is:

<p>\begin{align}
V_c = V_s(1 - e^{(\frac{t}{RC})})
\end{align}</p>

<p class="centered">
where:<br/>
\(V_c\) = voltage across the capacitor, Volts<br/>
\(V_s\) = supply voltage, Volts<br/>
\(t\) = time since supply was turned on, Seconds<br/>
\(R\) = resistance, Ohms<br/>
\(C\) = capacitance, Farads<br/>
</p>

This equation can be re-arranged to find the time `\(t\)`, and which the capacitor is at a certain voltage:

<p>\begin{align}
t = -log(\frac{V-V_c}{V})RC
\end{align}</p>

This form of the equation can be useful to calculate the delay (aka the time `\(t\)`), that the RC circuit will provide before something happens.


### Building A VDAC From An ADC And Low-pass RC Filter

**Low-pass RC filters can also be used to create a VDAC (voltage-based digital-to-analogue converter) from a [PWM signal](/electronics/circuit-design/pulse-width-modulation-pwm).** This is useful since many microcontrollers have one (or more) PWM peripherals, but rarely a built-in VDAC. A simple RC filter placed on the output pin of the PWM signal can convert it into a VDAC, in where the **duty cycle** determines the analogue voltage output.

### Low-Pass LC Filter

The basic low-pass LC filter consists of a single inductor and capacitor.

{{% figure src="low-pass-lc-filter-schematic.svg" width="556px" caption="A basic schematic of a low-pass LC filter." %}}

Unlike the low-pass RC filter, the low-pass LC filter is theoretically loss-less. This means that it does not dissipate energy as heat. However, real-world inductors have coil resistance and magnetic losses, as well as ESR in the capacitor. Also, the presence of the inductance usually makes the LC filter larger and more expensive than the RC filter.

This makes an LC low-pass filter suitable for higher-power applications. You will see LC low-pass filters being used on the output of [buck converters](/electronics/components/power-regulators/switch-mode-power-supplies-smps/) (they are essentially part of the buck converter), to filter the output of an H-bridge, and to filter audio signals before they reach the speakers.

The cut-off frequency of a low-pass LC filter is given by the following equation:

<p>\begin{align}
f_c = \frac{1}{2\pi \sqrt{LC}}
\end{align}</p>

The characteristic impedance is:

<p>\begin{align}
Z = \sqrt{LC}
\end{align}</p>

which you will notice is also present in the cut-off frequency equation.

#### Parasitic elements

The main parasitic element to consider with a low-pass LC filter is the parasitic coil resistance of the inductor, `\(R_L\)`. Larger valued inductors typically have a larger coil resistance (due to more windings). This dampens the output signal.

{{% figure src="low-pass-lc-filter-with-parasitics-schematic.png" width="539px" caption="A schematic of a LC low-pass filter with parasitic inductor resistance included." %}}

This is equivalent to a low-pass RLC filter.

### Low-pass RLC Filter

The quality factor is equal to:

<p>\begin{align}
Q = \frac{2\pi f}{R}
\end{align}</p>

As you increase the series resistance, the quality factor decreases.

The damping factor is equal to:

<p>\begin{align}
d_0 &= \frac{1}{Q} \\
d_0 &= \frac{R}{2\pi fL} \\
\end{align}</p>

### Low-Pass Pi And t Filters

Low-pass Pi (π) and t-filters are one step better than the low-pass LC or RC filter.

A 1st-order low-pass π-filter has two capacitors and one inductor. The first capacitor absorbs the most AC by shunting it to ground (assuming the input has a finite source impedance). The inductor then blocks remaining AC, allowing only DC to pass through to the second capacitor. The second capacitor then shunts any remaining AC signal back through ground.

The equations for a 1st order filter are:

<p>\begin{align}
C   &= \frac{z_o}{\pi f_c} \\
L   &= \frac{1}{z_o \pi f_c} \\
f_c &= \frac{1}{\pi \sqrt{LC}} \\
\end{align}</p>

<p class="centered">
where:<br/>
\(C\) = total capacitance in \(F\)<br/>
\(L\) = total inductance, in \(H\)<br/>
\(z_o\) = characteristic impedance, in \(\Omega\)<br/>
\(f_c\) = -3dB cut-off frequency, in \(Hz\)<br/>
</p>

{{% note %}}
Mentioned is total capacitance or total inductance, as in the case of the π-filter each capacitor is C/2, and in the case of the t-filter, each inductor is L/2.
{{% /note %}}

The typical value to use for the characteristic impedance is `\( z_o = 50 \Omega \)`. Use this if you are unsure on what to set it to. This value is only important if your are matching two RF circuits.

A t-filter is usually better at suppressing high-frequencies than a π-filter, as parasitic coupling between input and output due to PCB layout tends to turn the π filter into a notch filter. However, π-filters are more common because they are cheaper (capacitors are cheaper than inductors).

Both π and t filters may use [feedthrough capacitors](/electronics/components/capacitors#feedthrough-capacitors) instead of standard caps for better performance (feedthrough capacitors have lower parasitic series inductance).

### Pre-packaged Pi And T Filters

π and t filters can come in pre-packaged components which take all the hassle out of designing the filter correctly and reduce the BOM count of your design. They are commonly in [EIAxxxx chip packages](/pcb-design/component-packages/chip-eia-component-packages/).

One such example is the [TDK Corporation MEM Series](http://www.digikey.com/product-search/en?FV=ffec061a).

## 2nd-Order Passive Filters

This chaining is also called _cascading_. The benefit of doing this is that a second-order filter has a roll-off of -40dB/decade, twice that of a first-order filter.

### Second-Order Low-Pass RC

The corner frequency `\(f_c\)` is equal to:

<p>\begin{align}
f_c = \frac{1}{2\pi \sqrt{R_1 C_1 R_2 C_2}}
\end{align}</p>

Is is important to remember that for a second-order filter, the gain at the corner frequency is no longer -3dB. Instead it is -6dB. In general, the gain can be described for `\(n\)` stages with:

<p>\begin{align}
G = \left( \frac{1}{\sqrt{2}} \right) ^n
\end{align}</p>

The reduce the effects of each stages dynamic impedance effecting it's neighbours, its recommended that the following stages resistance should be around 10x the previous stage, and the capacitance 1/10th of the previous stage.

### Passive RC Networks With Voltage Gain > 1

It might seem hard to believe, but you can build RC networks which increase the input voltage at specific frequencies. See [Herman Epstein - Synthesis Of Passive RC Networks With Gains Greater Than Unity](http://www.oldfriend.url.tw/article/IEEE_paper/Synthesis%20of%20Passive%20RC%20Networks%20with%20Gains.pdf) [(cached copy, 2021-01-23)](./herman-epstein-synthesis-of-passive-rc-networks-with-gains-greater-than-unity.pdf) for a detailed analysis.

## Filter Tunings

_Filter tunings_ are specific tunings of filters to maximise a particular characteristic of it's response. Filter tuning directly specifies what the filters polynomials must be.

* **Butterworth** Optimized for the flattest response through the pass-band, at the expense of having a low transition between the pass and stop-band.
* **Chebyshev**: Designed to have a steep transition between the pass and stop-band, at the expense of gain ripple in either the pass or stopband (_type 1_ or _type 2_). Also called  Chevyshev, Tschebychev, Tschebyscheff or Tchevysheff, depending on exactly how you translate the original Russian name. There are two types of Chebyshev filters:
    * **Type 1:** _Type 1 Chebyshev filters_ (a.k.a. just a _Chebyshev filter_) have ripple in the passband, but no ripple in the stopband.
    * **Type 2:** _Type 2 Chebyshev filters_ (a.k.a. an _inverse Chebyshev filter_) have ripple in the stopband, but no ripple in the passband.
* **Bessel**: Optimized for linear phase response up to (or down to for high-pass filters) the cutoff frequency `\(f_c\)`, at the expense of a slower transition to the stop-band. This is useful to minimizing the signal distortion (a linear _phase response_ in the frequency domain is a constant _time delay_ in the time domain).
* **Elliptic:** Designed to have the fastest transition from the passband to the stopband, at the expense of ripple in both of these bands (Chebyshev optimization only produces ripple in one of the bands but is not as fast in the transition). Also called _Cauer_ filters or _Rational Chebyshev_ filters.

The graphs below show the differences in response (bode plots, gain and phase) for these various filter tunings:

{{% figure src="low-pass-filter-optimization-comparison-gain-db.png" width="700px" caption="A comparison of different filter optimizations. Gain shown in dB." %}}

Sometimes the differences can been visualized better by display the gain as `\(V/V\)`:

{{% figure src="low-pass-filter-optimization-comparison-gain-vv.png" width="700px" caption="A comparison of different filter optimizations. Gain shown in V/V." %}}

The linear phase delay of the Bessel filter is best visualized in the below plot where the phase in plotted on a linear scale rather than a logarithmic:

{{% figure src="low-pass-filter-optimization-comparison-phase-linear.png" width="700px" caption="Phase delay of different filter optimizations, with the frequency plotted on a linear axis rather than a logarithmic axis. This is the best way to visualize the linear phase delay of the Bessel optimization." %}}

### Butterworth Tunings

The normalized Butterworth polynomial of degree `\(n\)` is given by[^bib-pieter-p-butterworth-filters]:

<p>\begin{align}
\label{eq:butterworth-polynomial}
B_n(s) =
\begin{cases}
  \prod_{k=0}^{\frac{n}{2} - 1}(s^2 -2\cos{(2\pi\frac{2k + n + 1}{4n})s + 1}) & \text{even }n \\
  (s + 1)\prod_{k=0}^{\frac{n - 1}{2} - 1}(s^2 -2\cos{(2\pi\frac{2k + n + 1}{4n})s + 1}) & \text{odd }n \\
\end{cases}
\end{align}</p>

{{% tip %}}
If you've never seen it before, the large Pi symbol `\(\prod\)` in the above equation represents the product of a series of things, such like the capital Sigma symbol `\(\Sigma\)` represents the sum of a series of things. For example, `\(\prod_{k=1}^{3}k = 1\times 2 \times 3\)`.
{{% /tip %}}

Below is a table of the factored Butterworth polynomials for order `\(n\)`. The polynomial is useful in this form as each product forms either a first or second-order partial filter which can be directly implemented by a standard filter topology (e.g. RC filter for a first-order section, Sallen-Key for a second-order section). These polynomials were generated with `\(Eq.\ \ref{eq:butterworth-polynomial}\)`.

<table>
 <thead>
  <tr>
   <th style="text-align: right;">
    n
   </th>
   <th style="width: 700px;">
    poly
   </th>
  </tr>
 </thead>
 <tbody>
  <tr>
   <td style="text-align: right;">
    1
   </td>
   <td>
    \((s + 1)\)
   </td>
  </tr>
  <tr>
   <td style="text-align: right;">
    2
   </td>
   <td>
    \((s^{2} + 1.414 s + 1)\)
   </td>
  </tr>
  <tr>
   <td style="text-align: right;">
    3
   </td>
   <td>
    \(\left(s + 1\right) \left(s^{2} + 1.0 s + 1\right)\)
   </td>
  </tr>
  <tr>
   <td style="text-align: right;">
    4
   </td>
   <td>
    \(\left(s^{2} + 0.765 s + 1\right) \left(s^{2} + 1.848 s + 1\right)\)
   </td>
  </tr>
  <tr>
   <td style="text-align: right;">
    5
   </td>
   <td>
    \(\left(s + 1\right) \left(s^{2} + 0.618 s + 1\right) \left(s^{2} + 1.618 s + 1\right)\)
   </td>
  </tr>
  <tr>
   <td style="text-align: right;">
    6
   </td>
   <td>
    \(\left(s^{2} + 0.518 s + 1\right) \left(s^{2} + 1.414 s + 1\right) \left(s^{2} + 1.932 s + 1\right)\)
   </td>
  </tr>
  <tr>
   <td style="text-align: right;">
    7
   </td>
   <td>
    \(\left(s + 1\right) \left(s^{2} + 0.445 s + 1\right) \left(s^{2} + 1.247 s + 1\right) \left(s^{2} + 1.802 s + 1\right)\)
   </td>
  </tr>
  <tr>
   <td style="text-align: right;">
    8
   </td>
   <td>
    \(\left(s^{2} + 0.39 s + 1\right) \left(s^{2} + 1.111 s + 1\right) \left(s^{2} + 1.663 s + 1\right) \left(s^{2} + 1.962 s + 1\right)\)
   </td>
  </tr>
 </tbody>
</table>

### Chebyshev Optimization

Chebyshev filters with even order numbers (e.g. 2nd order, 4th order, ...) generate ripples above the 0dB line, filters with odd order numbers (e.g. 3rd order, 5th order, ...) generate ripples below the 0dB line.

Because Chebyshev filters have ripple in the pass-band, **their cutoff frequency is usually defined in a completely different way to all other filter optimizations**. Rather than specifying `\(f_c\)` as the -3dB point, the `\(f_c\)` for Chebyshev filters is defined at the point at which the gain leaves the allowed ripple region (i.e. > 0.5dB for a 0.5dB Chebyshev filter, > 3dB for a 3dB Chebyshev filter).

### Bessel Optimization

Commonly used in analogue-crossover circuitry.

### Elliptic Optimization

Elliptic optimization (a.k.a. a Cauer or Zolotarev filter[^bib-rutgers-elliptic-lecture-notes]) is a filter that is optimized for the fastest transition in gain from the passband to the stopband. It has equal ripple in both the passband and stopband[^bib-wikipedia-elliptic-filter].

You can generate an Elliptical filter in Python using the scipy package:

```python
scipy.signal.ellip(N, rp, rs, Wn, btype='low', analog=False, output='ba', fs=None)
```

### Filter Coefficient Tables

* `\(n\)` is the filter order
* `\(i\)` is the partial filter order
* `\(a_i\)` and `\(b_i\)` are the filter coefficients
* `\(k_i\)` is the ratio between the corner frequency of the partial filter `\(f_{ci}\)` and the corner frequency of the overall filter `\(f_c\)`. In equation form:
    <p>\begin{align}k_i = \frac{f_{ci}}{f_c} \end{align}</p>
* `\(Q_i\)` is the quality factor of the partial filter

All values have been normalized by setting `\(\omega_c = 1\)`.

#### Butterworth Coefficients

<table>
  <thead>
    <tr><th>n</th>  <th>\(i\)</th>  <th>\(a_i\)</th>  <th>\(b_i\)</th>  <th>\(k_i\)</th>  <th>\(Q_i\)</th>  <th style="width: 200px;">Polynomial Factors</th></tr>
  </thead>
  <tbody>
    <tr><td>1</td>      <td>1</td>      <td>1.0000</td>   <td>0.0000</td>   <td>1.000</td>    <td>n/a</td>  <td>\(s + 1\)</td></tr>
    <tr><td>2</td>      <td>1</td>      <td>1.4142</td>   <td>1.0000</td>   <td>1.000</td>    <td>0.71</td> <td>\(s^2 + 1.4142s + 1\)</td></tr>
    <tr><td>3</td>      <td>1</td>      <td>1.0000</td>   <td>0.0000</td>   <td>1.000</td>    <td>n/a</td>  <td rowspan="2">\((s + 1)(s^2 + s + 1)\)</td></tr>
    <tr><td></td>       <td>2</td>      <td>1.0000</td>   <td>1.0000</td>   <td>1.272</td>    <td>1.00</td></tr>
  </tbody>
</table>



#### Chebyshev Coefficients For 3dB Passband Ripple

<table>
  <thead>
    <tr><th>n</th>  <th>\(i\)</th>  <th>\(a_i\)</th>  <th>\(b_i\)</th>  <th>\(k_i\)</th>  <th>\(Q_i\)</th></tr>
  </thead>
  <tbody>
    <tr><td>1</td>      <td>1</td>      <td>1.0000</td>   <td>0.0000</td>   <td>1.000</td>    <td>n/a</td></tr>
    <tr><td>2</td>      <td>1</td>      <td>1.0650</td>   <td>1.9305</td>   <td>1.000</td>    <td>1.30</td></tr>
    <tr><td>3</td>      <td>1</td>      <td>2.7994</td>   <td>0.0000</td>   <td>0.357</td>    <td>n/a</td></tr>
    <tr><td></td>       <td>2</td>      <td>0.4300</td>   <td>1.2036</td>   <td>1.378</td>    <td>2.55</td></tr>
  </tbody>
</table>

#### Bessel Coefficients

<table>
  <thead>
    <tr><th>n</th>  <th>\(i\)</th>  <th>\(a_i\)</th>  <th>\(b_i\)</th>  <th>\(k_i\)</th>  <th>\(Q_i\)</th></tr>
  </thead>
  <tbody>
    <tr><td>1</td>      <td>1</td>      <td>1.0000</td>   <td>0.0000</td>   <td>1.000</td>    <td>n/a</td></tr>
    <tr><td>2</td>      <td>1</td>      <td>1.3617</td>   <td>0.6180</td>   <td>1.000</td>    <td>0.58</td></tr>
    <tr><td>3</td>      <td>1</td>      <td>0.7560</td>   <td>0.0000</td>   <td>1.323</td>    <td>n/a</td></tr>
    <tr><td></td>       <td>2</td>      <td>0.9996</td>   <td>0.4772</td>   <td>1.414</td>    <td>0.69</td></tr>
  </tbody>
</table>

### 2nd Order Filter Topologies

A filter topology is an actual circuit configuration which can realize a number of different filter designs. This is different from the configurations such as Butterworth, Chebyshev and Bessel which define the component tuning

* Sallen-Key (a.k.a. KRC filters)
* Tow-Thomas
* Multiple-Feedback Filters (a.k.a. infinite-gain filters)
* State-Variable Filters: As known as _KHN filters_ after the inventors W. J. Kerwin, L. P. Huelsman and R. W. Newcomb, first reported in 1967[^bib-sergio-franco-design-with-op-amps].

## Voltage-Controlled Voltage-Source (VCVS) Filters

Voltage-controlled voltage-source (VCVS) filters are an extension of the [Sallen-Key filter](#sallen-key-filters) (in that sense, the _Sallen-Key filter_ can be thought of as a simplification of the VCVS filter in where the voltage gain of the op-amp is set to one) in where standard resistor divider feedback is added between the op-amp's output and the inverting input, allowing the gain of the filter to be something other than `\(1\)`.

They are called VCVS filters because the op-amp is used as a voltage amplifier.

{{% figure src="low-pass-vcvs-generic/low-pass-vcvs-generic.svg" width="700px" caption="Schematic of a generic VCVS filter. Note how it is very similar to the Sallen-Key filter, except with the additional resistors R3 and R4 to set a voltage gain other than unity." %}}

## Design Tools

### OKAWA Filter Design and Analysis

Website: [http://sim.okawa-denshi.jp/en/Fkeisan.htm](http://sim.okawa-denshi.jp/en/Fkeisan.htm)

Great site with web-based calculators and design tools for active and passive filters. Very detailed site with many configuration options and the site even outputs graphs of your designed filter response.

{{% figure src="okawa-filter-design-and-analysis-homepage-screenshot.png" width="700px" caption="Screenshot of the homepage for the OKAWA Filter Design and Analysis website. Image from http://sim.okawa-denshi.jp/en/Fkeisan.htm, retrieved 2021-03-27." %}}

### PSoC Microcontrollers And The PSoC Creator IDE

The PSoC microcontroller features an in-built and versatile digital filter block, and the IDE has a graphically-edited method of configuring the DFB to do exactly what you want. The IDE even shows you graphs of the expected response (magnitude, phase, step plots e.t.c).

## External Resources

* The [New Jersey Institute of Technology EE 494 Laboratory IV Part B lab manual](https://web.njit.edu/~gilhc/EE494/ee494b.pdf) is a great practical resource for learning how to design active filters.
* The [Design With Operational Amplifiers And Analog Integrated Circuits by Sergio Franco, Fourth Edition](https://www.mheducation.com/highered/product/design-operational-amplifiers-analog-integrated-circuits-franco/M9780078028168.html) is a great book to purchase if you are interesting in further reading and getting right into the weeds of analogue filter design!
* [Op Amps For Everyone by Ron Mancini (SLOD006B)](https://web.mit.edu/6.101/www/reference/op_amps_everyone.pdf) has some detailed sections on op-amp filter circuits.
* [SLOA024B: Analysis of the Sallen-Key Architecture - Application Report, by Texas Instruments](https://www.ti.com/lit/an/sloa024b/sloa024b.pdf) can be used for further reading on the Sallen-Key and VCVS amplifiers (<a href="sloa024b-analysis-of-the-sallen-key-architecture-application-report-texas-instruments.pdf" download>cached local copy</a>).
* Texas Instruments [Filter Designer](https://www.ti.com/design-resources/design-tools-simulation/filter-designer.html) is a free online tool to design filters.
* The Analog Devices [Filter Wizard](https://tools.analog.com/en/filterwizard/) is an alternative to the Texas Instruments version.   

## References

[^bib-wikipedia-low-pass-filter]:  Wikipedia. _Low-pass filter_. Retrieved 2021-03-25, from https://en.wikipedia.org/wiki/Low-pass_filter.
[^bib-elec-tutorial-filters]:  Electronic Tutorials. _Passive Low Pass Filter_. Retrieved 2021-03-25, from https://www.electronics-tutorials.ws/filter/filter_2.html.
[^bib-sergio-franco-design-with-op-amps]:  Franco, Sergio. _Design With Operational Amplifiers And Analog Integrated Circuits_. Fourth Edition. McGraw-Hill Education. Copyright 2015.
[^bib-wikipedia-elliptic-filter]: Wikipedia (2022, Jan 30). _Elliptic filter_. Retrieved 2022-09-20, from https://en.wikipedia.org/wiki/Elliptic_filter.
[^bib-rutgers-elliptic-lecture-notes]: Sophocles J. Orfanidis (2006, Nov 20). _Lecture Notes on Elliptic Filter Design_. Rutgers University: Department of Electrical & Computer Engineering. Retrieved 2022-09-20, from https://www.ece.rutgers.edu/~orfanidi/ece521/notes.pdf.
[^bib-analog-devices-ch8-analog-filters]: Analog Devices. _Chapter 8: Analog Filters_. Retrieved 2022-09-20, https://www.analog.com/media/en/training-seminars/design-handbooks/Basic-Linear-Design/Chapter8.pdf.
[^bib-pieter-p-butterworth-filters]: Pieter P (2021, Jul 15). _Butterworth Filters_. Retrieved 2022-10-06, from https://tttapa.github.io/Pages/Mathematics/Systems-and-Control-Theory/Analog-Filters/Butterworth-Filters.html.