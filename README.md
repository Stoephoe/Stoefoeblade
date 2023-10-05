# Tegenwindauto Turbinebladen Ontwerptool "Stoefoeblade"

Welkom bij de Tegenwindauto Turbinebladen Ontwerptool! In deze repository vind je alle benodigde informatie en scripts voor het optimaliseren van de twist en cordelengte van turbinebladen voor een tegenwindauto. Deze software is gebaseerd op de BEM-theorie voor dynamische turbines, zoals beschreven door Mac Gaunaa. Voor meer details over deze theorie kun je ons bijgevoegde verslag raadplegen.

## Doel

Het hoofddoel van deze ontwerptool is om het twist- en cordelengteprofiel van de turbinebladen te optimaliseren voor maximale efficiëntie.

## Werking

De software is ontworpen als een eenvoudige implementatie van de eerder genoemde BEM-theorie. Het script start met een aantal aangenomen waarden, waarvan de belangrijkste de inductiefactor 'a' is, die is ingesteld op 0. De software maakt gebruik van een eenvoudige rekenlus. De gebruiker kan een bereik definiëren waarin cordelengtes worden bepaald. Voor elke tussenliggende cordelengte worden de aerodynamische eigenschappen berekend. De gebruiker kan ook de resolutie van cordelengtes aanpassen.

## Invoerparameters

Om de software te gebruiken, moet je de volgende invoerparameters specificeren:

- `U_free`: Snelheid van de aanstromende vrije wind in m/s
- `Eff_v`: Gewenste verhouding tussen de rijsnelheid en windsnelheid [0, 1]
- `Eff_t`: Efficiëntie van de transmissie (aangenomen op 80%, dus 0.8) [0, 1]
- `Eff_p`: Efficiëntie van de Aandrijflijn (aangenomen op 80%, dus 0.8) [0, 1]
- `TSR`: Gewenste Tipspeed ratio (tipsnelheid)
- `D_t`: Turbinediameter (inclusief diffuser) in meters
- `D_r`: Diffuserdiameter in meters
- `D_h`: Hubdiameter in meters
- `N_seg`: Gewenste hoeveelheid dwarsdoorsnede segmenten per blad
- `Blades`: Gewenste hoeveelheid bladen
- `Max_c`: Gewenste maximale cordelengte in meters
- `Min_c`: Gewenste minimale cordelengte in meters
- `Res_c`: Gewenste cordelengteresolutie [0, 1000]
- `Rotorfoil`: Gewenst te gebruiken profiel
- `Max_itt_BEM`: Gewenste hoeveelheid BEM-iteraties per cordelengte

## Bekende Problemen

Houd rekening met de volgende bekende problemen bij het gebruik van deze ontwerptool:

1. **Optimalisatie werkt niet met verkeerd cordelengte bereik:** Het is cruciaal om een geschikt cordelengtebereik te specificeren. Een verkeerd bereik kan leiden tot onjuiste optimalisatie-uitkomsten.

2. **Inductiefactor zorgt vaak voor afwijkende resultaten:** De inductiefactor 'a' kan variabele resultaten opleveren en is gevoelig voor invoerwaarden. Wees voorzichtig bij het interpreteren van resultaten die sterk afhankelijk zijn van 'a'.

3. **Resultaten zijn niet representatief, maar wel correct als er wordt gerekend met verhoudingen:** Houd er rekening mee dat de resultaten mogelijk niet direct representatief zijn voor praktische toepassingen. Ze zijn vooral bedoeld voor vergelijkingen op basis van verhoudingen en relatieve optimalisaties.

4. **Erg rudimentair:** Deze software is ontworpen als een rudimentaire implementatie van de BEM-theorie. Geavanceerde functies en complexe scenario's kunnen beperkt worden ondersteund.

## Aan de slag

Wil je aan de slag met het ontwerpen van turbinebladen voor de Tegenwindauto? Volg dan het stapsgewijze proces en raadpleeg onze handleiding voor gedetailleerde instructies. We hebben ook een lijst met bekende bugs en oplossingen opgenomen in de handleiding voor jouw gemak.

## Meer informatie

Voor meer informatie over de achtergrond van de gebruikte theorie en technieken, raden we je ten zeerste aan om ons bijgevoegde verslag te lezen. Hierin wordt de gebruikte theorie verder uitgelegd en gedetailleerd beschreven.

We hopen dat deze ontwerptool je helpt bij het optimaliseren van de turbinebladen voor de Tegenwindauto. Veel succes en veel plezier met ontwerpen!
