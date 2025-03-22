import random
import pandas as pd
from datetime import datetime, timedelta
# Mögliche typs: Einbruch, Demonstrationen, Wirtschaft, Infos um die Königfamilie (schwangerschaften etc), angekündigte Veranstalltungen (Pferderennen, Jahrmarkt, Schiffseinweihung etc), Feste (sowohl volksfeste als auch ostern, weinachten etc. mit special_dates)
# Probability: 1 (low), 2 (medium), 3 (high), 0 (wenn ein followup_newspaper)

def creat_dataframe():
    columns = ["newspaper_event_id", "short_description", "newspaper_text", "activation_boolean", "follow_newspaper_id", "follow_newspaper_time_break", "probability", "typ", "spezial_date"]
    newspaper = [
        (3, "Maschinenstürmer greifen Weberei in Leeds an", 
        "In der vergangenen Nacht wurde die Weberei Brown & Sons Ziel eines wütenden Mobs. Die Maschinenstürmer protestierten gegen die Einführung neuer Maschinen, die ihrer Meinung nach die Arbeitsplätze der Textilarbeiter bedrohten. Der Angriff führte zu schweren Schäden an den Maschinen, doch es gab keine Berichte über Verletzte. Die Polizei konnte die Situation nicht schnell genug unter Kontrolle bringen, da die Demonstranten in großer Zahl auftraten. Weitere Ausschreitungen werden befürchtet.", 
        True, 4, 3, 3, "Demonstrationen", "12.04"),

        (4, "Prozess gegen Maschinenstürmer beginnt", 
        "Heute begann in Leeds der Prozess gegen die fünf festgenommenen Maschinenstürmer. Die Angeklagten stehen unter Anklage wegen Sachbeschädigung und Aufruhr. Ihre Verteidiger argumentieren, dass die Proteste als Ausdruck des Widerstandes gegen die Ausbeutung der Arbeiterklasse zu werten sind. Die Staatsanwaltschaft hingegen betont die Schwere der Schäden und die Gefährdung der öffentlichen Ordnung. Das Urteil wird in den kommenden Wochen erwartet.", 
        False, None, None, 0, "Demonstrationen", "15.04"),

        (5, "Eröffnung der neuen Eisenbahnstrecke Manchester-Liverpool", 
        "Mit großem Jubel wurde heute die neue Eisenbahnverbindung zwischen Manchester und Liverpool eingeweiht. Der Zug fährt in rekordverdächtiger Geschwindigkeit und soll die wirtschaftliche Verbindung zwischen den beiden Städten erheblich verbessern. Die Eröffnung wurde von zahlreichen Persönlichkeiten des öffentlichen Lebens begleitet, die die Bedeutung dieses Projekts für die Region betonten. Es wird erwartet, dass die Strecke nicht nur den Handel, sondern auch den Tourismus ankurbeln wird.", 
        True, None, None, 3, "Wirtschaft", "01.05"),

        (6, "Skandal auf Ball der Londoner Gesellschaft", 
        "Der diesjährige Frühlingsball im Herrenhaus von Lord Kensington endete mit einem Skandal. Während der Feierlichkeiten wurde eine verbotene Liebesaffäre zwischen einem verheirateten Politiker und einer prominenten Gesellschaftsdame enthüllt. Der Vorfall sorgte für Aufregung in den Kreisen der Londoner Oberschicht und löste eine öffentliche Diskussion über Moral und den Druck, der auf den Eliteangehörigen lastet, aus. Der betroffene Politiker hat sich bisher nicht öffentlich zu den Vorwürfen geäußert.", 
        False, None, None, 2, "Gesellschaft", "10.05"),

        (7, "Jahrmarkt in York lockt tausende Besucher", 
        "Der traditionelle Jahrmarkt in York eröffnete gestern seine Pforten und lockte bereits am ersten Tag eine beeindruckende Menge an Besuchern an. Die zahlreichen Stände, Fahrgeschäfte und Unterhaltungseinrichtungen sorgten für eine festliche Atmosphäre. Die lokalen Händler berichteten von einem Anstieg der Verkäufe und einer generell positiven Stimmung in der Stadt. Der Jahrmarkt wird voraussichtlich noch eine weitere Woche geöffnet bleiben und gilt als eines der wichtigsten jährlichen Ereignisse in York.", 
        True, None, None, 3, "Veranstaltung", "20.06"),

        (9, "Geheimbund in London entdeckt", 
        "Die Polizei hat in einem Lagerhaus nahe dem Hafen eine geheime Versammlung eines bislang unbekannten Geheimbundes aufgelöst. Der Geheimbund, dessen Mitglieder sich gegen die Obrigkeit aussprachen, hatte bereits Pläne für mehrere Aktionen gegen die Regierung in Vorbereitung. Bei der Durchsuchung wurden Dokumente und Waffen sichergestellt. Der Fall hat für Aufsehen gesorgt und viele spekulieren, dass auch hochrangige Persönlichkeiten in den Bund verwickelt sein könnten.", 
        True, None, None, 3, "Infos um die Königsfamilie", "05.07"),

        (10, "Explosion erschüttert Chemiefabrik", 
        "Ein schweres Unglück ereignete sich in einer Chemiefabrik in Birmingham. Bei einer Explosion wurden mehrere Gebäude zerstört, und es gab zahlreiche Verletzte. Die Ursache des Unglücks ist derzeit noch unklar, jedoch wird ein technischer Defekt als mögliche Ursache vermutet. Rettungsteams arbeiten mit Hochdruck an der Bergung von Überlebenden, während die Feuerwehr die brennenden Ruinen löscht. Der Vorfall hat auch Bedenken hinsichtlich der Sicherheitsvorkehrungen in der chemischen Industrie aufgeworfen.", 
        True, None, None, 3, "Wirtschaft", "22.07"),

        (12, "Unruhen auf dem Marktplatz von Edinburgh", 
        "Wütende Händler lieferten sich eine Auseinandersetzung mit städtischen Beamten, nachdem neue Handelsabgaben angekündigt wurden. Die Proteste eskalierten schnell, und es kam zu gewaltsamen Auseinandersetzungen. Die Polizei musste einschreiten, um die Unruhen zu beenden. Mehrere Festnahmen wurden vorgenommen, und es gab Berichte über Verletzte. Die Stadtverwaltung hat angekündigt, die Situation zu überprüfen und mögliche Änderungen der Abgabenstruktur in Erwägung zu ziehen.", 
        True, 13, 2, 3, "Demonstrationen", "02.08"),

        (13, "Stadtverwaltung lenkt nach Protesten ein", 
        "Nach den heftigen Protesten auf dem Marktplatz von Edinburgh hat die Stadtverwaltung angekündigt, die neuen Handelsabgaben zu überarbeiten. Es wird erwartet, dass die Regierung in den kommenden Tagen eine Erklärung abgibt, wie sie den Forderungen der Händler entgegenkommen wird. Der Stadtrat betonte, dass die Situation schnell gelöst werden muss, um weitere Unruhen zu vermeiden. Der Rückzug der neuen Abgaben gilt als ein erster Schritt zur Beruhigung der Lage.", 
        False, None, None, 0, "Demonstrationen", "05.08"),

        (14, "Königin Victoria besucht die Royal Navy", 
        "In einer feierlichen Zeremonie inspizierte Königin Victoria die neueste Flotte der Royal Navy. Während ihres Besuchs sprach sie mit mehreren Admiralen und Offizieren über die aktuellen Herausforderungen der Marine. Die Königin lobte die hervorragende Arbeit der Navy und betonte ihre Bedeutung für die nationale Sicherheit. Der Besuch gilt als ein symbolischer Akt der Unterstützung für die Streitkräfte des Vereinigten Königreichs.", 
        False, None, None, 3, "Infos um die Königsfamilie", "15.08"),

        (15, "Schwere Überschwemmungen in Wales", 
        "Starke Regenfälle haben in Wales zu schweren Überschwemmungen geführt. Zahlreiche Dörfer sind von den Fluten betroffen, und viele Häuser wurden zerstört. Rettungsdienste sind im Einsatz, um Menschen aus den gefährdeten Gebieten zu evakuieren. Der Schaden an der Infrastruktur ist erheblich, und die Behörden haben mitgeteilt, dass der Wiederaufbau der betroffenen Gebiete Wochen dauern könnte. Die Bevölkerung wird aufgerufen, sich in Sicherheit zu bringen und keine Reisen in die betroffenen Gebiete zu unternehmen.", 
        True, None, None, 2, "Infos um die Königsfamilie", "25.08"),

        (17, "Erster dampfbetriebener Omnibus in London", 
        "Ein neuer dampfbetriebener Omnibus wurde erfolgreich auf Londons Straßen getestet. Das Fahrzeug, das eine völlig neue Art der Personenbeförderung darstellt, soll künftig die Straßen von London entlasten und den Verkehr revolutionieren. Das innovative Transportmittel wurde von mehreren prominenten Persönlichkeiten aus der Wirtschaft und Politik gefeiert. Der Omnibus soll in den kommenden Wochen in regulären Betrieb gehen.", 
        True, None, None, 3, "Wirtschaft", "10.09"),

        (19, "Schmugglerring in Dover ausgehoben", 
        "Die Zollbehörden haben einen groß angelegten Schmugglerring in Dover zerschlagen. Bei einer Razzia wurden mehrere Verdächtige festgenommen und große Mengen illegaler Waren sichergestellt. Die Schmuggler hatten das Ziel, Waren wie Alkohol und Tabak ohne die fälligen Zölle ins Land zu bringen. Die Festnahmen wurden von der Polizei als wichtigen Erfolg im Kampf gegen den illegalen Handel bezeichnet.", 
        True, None, None, 3, "Einbruch", "05.10"),

        (21, "Skandal um hochrangigen Politiker", 
        "Ein ranghoher Minister gerät unter Druck, nachdem geheime Dokumente an die Presse durchgesickert sind. Die Dokumente enthalten brisante Informationen, die möglicherweise die nationale Sicherheit betreffen. Der Minister hat bisher keine Stellungnahme abgegeben, aber die Opposition fordert seinen Rücktritt. Der Skandal sorgt für Turbulenzen in der Regierung, und Experten warnen vor den möglichen politischen Konsequenzen.", 
        True, None, None, 3, "Infos um die Königsfamilie", "12.11"),

        (22, "Neue Kanalverbindung geplant", 
        "Die Regierung hat den Bau eines neuen Kanals angekündigt, der die Handelsverbindungen zwischen London und Birmingham verbessern soll. Das Projekt, das mit hohen Investitionen verbunden ist, soll den Transport von Gütern deutlich erleichtern und die Wirtschaft der beiden Städte stärken. Der Kanal wird voraussichtlich eine Länge von 80 Kilometern haben und auch die Schifffahrt für den internationalen Handel ankurbeln. Kritiker warnen jedoch vor den potenziellen Umweltfolgen, da ein solcher Eingriff in die Natur auch negative Auswirkungen haben könnte.", 
        False, None, None, 3, "Wirtschaft", "20.11"),

        (23, "Brand in der Nationalbibliothek", 
        "Ein Feuer in der Nationalbibliothek zerstörte wertvolle Manuskripte. Die Flammen brachen in den späten Nachtstunden aus und zerstörten große Teile der historischen Sammlung. Feuerwehrleute kämpften mehrere Stunden gegen das Feuer, konnten jedoch nicht verhindern, dass einige der ältesten und bedeutendsten Werke in Flammen aufgingen. Die Ursache des Feuers wird derzeit untersucht, und es wird befürchtet, dass es sich um Brandstiftung handelt. Experten sind besorgt über den Verlust von unvergleichbarem kulturellen Erbe.", 
        True, None, None, 3, "Einbruch", "30.11"),

        (24, "Ungewöhnlicher Meteoriteneinschlag in Cornwall", 
        "Ein Meteor schlug in der Nähe eines Bauernhofs in Cornwall ein. Der Einschlag ereignete sich in den frühen Morgenstunden und hinterließ einen großen Krater im Boden. Glücklicherweise gab es keine Verletzten, doch der Vorfall hat großes Aufsehen erregt. Wissenschaftler sind vor Ort, um den Meteoriten zu untersuchen, der aus einem bisher unbekannten Material zu bestehen scheint. Dieser Einschlag hat viele in der Region neugierig gemacht und es gibt bereits Gerüchte, dass es sich um ein ungewöhnliches Phänomen handeln könnte.", 
        False, None, None, 2, "Infos um die Königsfamilie", "05.12"),

        (26, "Geistererscheinungen im alten Herrenhaus?", 
        "Ein altes Herrenhaus in Dorset sorgt für Aufsehen, nachdem mehrere Bewohner von seltsamen Erscheinungen berichten. Zeugen berichten von mysteriösen Geräuschen, die in den Nächten durch die Flure hallen, sowie von Schatten, die sich selbst bei geschlossenen Türen bewegen. Einige Anwohner vermuten, dass es sich um übernatürliche Ereignisse handelt, während Skeptiker auf natürliche Erklärungen wie Schimmel oder alte Rohre hinweisen. Das Herrenhaus, das einst im Besitz einer adeligen Familie war, hat eine dunkle Geschichte, die von geheimen Treffen und dramatischen Ereignissen geprägt ist.", 
        False, None, None, 1, "Veranstaltung", "18.12"),

        (27, "Revolutionäre Erfindung in der Medizin", 
        "Ein Arzt aus Edinburgh hat eine neue Methode zur Wunddesinfektion entwickelt. Die Erfindung soll die Sterblichkeitsrate nach chirurgischen Eingriffen erheblich senken. Der Arzt, Dr. James McAlister, hat ein Verfahren entwickelt, das eine spezielle Mischung aus chemischen Substanzen verwendet, die Wunden vor Infektionen schützt und deren Heilung fördert. Die medizinische Gemeinschaft ist begeistert von dieser bahnbrechenden Entdeckung, die das Potenzial hat, die gesamte Praxis der Chirurgie zu revolutionieren.", 
        True, None, None, 3, "Wirtschaft", "22.12"),

        (28, "Rätselhafter Mord in Whitechapel", 
        "Ein wohlhabender Geschäftsmann wurde in einer dunklen Gasse von Whitechapel tot aufgefunden. Der Mord, der in der Nacht verübt wurde, hinterließ nur wenige Spuren, was die Ermittlungen erschwert. Die Polizei geht derzeit davon aus, dass der Geschäftsmann das Opfer eines Raubübergriffs wurde, doch es gibt auch Hinweise darauf, dass die Tat von jemandem begangen wurde, der dem Opfer nahe stand. Die Gerüchte über den Mord haben die Bewohner von Whitechapel in Aufregung versetzt, und es wird spekuliert, dass der Fall mit weiteren ungelösten Verbrechen in der Gegend in Verbindung stehen könnte.", 
        True, None, None, 3, "Einbruch", "27.12"),

        (30, "Dampfschiff explodiert im Hafen von Liverpool", 
        "Ein mit Kohle beladenes Dampfschiff explodierte im Hafen von Liverpool, wodurch mehrere Arbeiter ums Leben kamen. Das Unglück ereignete sich bei einem Ladevorgang, als eine plötzliche Explosion das Schiff in die Luft jagte. Zahlreiche Rettungskräfte sind vor Ort, um nach Überlebenden zu suchen, doch die Explosion hat bereits erhebliche Schäden an den benachbarten Docks angerichtet. Die Ursache der Explosion ist noch unklar, doch erste Untersuchungen deuten darauf hin, dass technische Mängel am Dampfkessel des Schiffes verantwortlich sein könnten. Die Behörden haben eine umfassende Untersuchung eingeleitet.", 
        True, None, None, 3, "Einbruch", "30.12"),

        (32, "Anschlag auf Minister verhindert", "Die Polizei konnte einen geplanten Anschlag auf einen hochrangigen Minister vereiteln. " "Drei Verdächtige wurden festgenommen, während die Hintergründe der Tat noch unklar sind.", True, None, None, 3, "Infos um die Königsfamilie", "2.5"),
        (33, "Erstes Telefonat zwischen London und Edinburgh", "Techniker führten erfolgreich das erste Telefonat zwischen London und Edinburgh durch. " "Experten sprechen von einem Meilenstein in der Telekommunikation.", False, None, None, 3, "Wirtschaft", "5.5"),
        (34, "Schwere Dürre in Nordengland", "Wochenlange Trockenheit hat in Nordengland zu schweren Ernteausfällen geführt. " "Die Regierung erwägt Maßnahmen zur Unterstützung betroffener Bauern.", True, None, None, 2, "Infos um die Königsfamilie", "10.5"),
        (35, "Diebstahl in der königlichen Kunstgalerie", "Unbekannte Diebe haben sich Zugang zur königlichen Kunstgalerie verschafft und ein wertvolles Gemälde entwendet. " "Die Ermittlungen laufen auf Hochtouren.", True, 36, 3, 3, "Einbruch", "12.5"),
        (36, "Gestohlenes Gemälde in Lagerhaus entdeckt", "Das vor wenigen Tagen gestohlene Gemälde aus der königlichen Kunstgalerie wurde in einem verlassenen Lagerhaus gefunden. " "Die Täter sind weiterhin flüchtig.", False, None, None, 0, "Einbruch", "16.5"),
        (37, "Sichtung in Schottland?", "Mehrere Bewohner eines schottischen Dorfes behaupten, ein fliegendes Objekt mit heller Beleuchtung gesehen zu haben. " "Wissenschaftler führen das Phänomen auf atmosphärische Störungen zurück.", False, None, None, 1, "Infos um die Königsfamilie", "20.5"),
        (38, "Erster Frauenclub in London gegründet", "Eine Gruppe engagierter Damen hat den ersten Club für Frauen in London ins Leben gerufen. " "Dort soll über politische und soziale Themen diskutiert werden – sehr zum Missfallen konservativer Kreise.", False, None, None, 3, "Gesellschaft", "25.5"),
        (39, "Eisenbahnarbeiter streiken für bessere Löhne", "Tausende Eisenbahnarbeiter legten ihre Arbeit nieder und fordern höhere Löhne sowie bessere Arbeitsbedingungen. " "Die Regierung zeigt sich bislang unnachgiebig.", True, None, None, 3, "Demonstrationen", "28.5"),
        (40, "Sensationsfund: Antikes Skelett entdeckt", "Bauarbeiter stießen bei Grabungen in Bath auf ein erstaunlich gut erhaltenes menschliches Skelett. " "Historiker spekulieren über die Herkunft der Überreste.", False, None, None, 2, "Wirtschaft", "1.6"),
        (41, "Großbrand in Londoner Textilfabrik", "Ein verheerender Brand zerstörte eine große Textilfabrik in Londons Osten. " "Hunderte Arbeiter stehen vor dem Nichts, während die Polizei Brandstiftung nicht ausschließt.", True, None, None, 3, "Einbruch", "4.6"),
        (42, "Erste Dampfautomobile im Testbetrieb", "Ein findiger Erfinder aus Manchester hat einen dampfbetriebenen Wagen entwickelt, der bald die Kutsche ersetzen könnte. " "Erste Tests verliefen vielversprechend.", False, None, None, 3, "Wirtschaft", "8.6"),
        (43, "Riesiges Walfossil vor Küste entdeckt", "Fischer fanden vor der Küste von Brighton die Überreste eines riesigen Walskeletts. " "Forscher reisen an, um das prähistorische Fossil zu untersuchen.", False, None, None, 2, "Infos um die Königsfamilie", "12.6"),
        (44, "Mysteriöses Verschwinden einer Adligen", "Die Tochter eines angesehenen Lords verschwand spurlos auf dem Heimweg von einer Abendgesellschaft. " "Spekulationen über eine Entführung oder eine heimliche Flucht kursieren in der Londoner Gesellschaft.", True, None, None, 3, "Gesellschaft", "15.6"),
        (45, "Jahrmarkt in Manchester mit neuer Attraktion", "Ein fahrendes Theater präsentiert auf dem diesjährigen Jahrmarkt in Manchester ein einzigartiges Steampunk-Spektakel. " "Besucher sind begeistert von den mechanischen Marionetten.", False, None, None, 2, "Veranstaltung", "18.6"),
        (46, "Historische Postkutsche entdeckt", "Ein Landwirt entdeckte eine alte Postkutsche, die offenbar seit Jahrzehnten in einem Wald verborgen lag. " "Archäologen untersuchen den Fund, der als Relikt aus Napoleons Zeiten gilt.", False, None, None, 2, "Wirtschaft", "22.6"),
        (47, "Bürgermeister von York wegen Korruption verhaftet", "Der Bürgermeister von York wurde wegen Korruptionsvorwürfen festgenommen. " "Er soll öffentliche Gelder veruntreut haben.", True, None, None, 3, "Infos um die Königsfamilie", "25.6"),
        (48, "Neuer Anbau von Tee in Cornwall", "Ein Landbesitzer hat mit dem Anbau von Tee in Cornwall begonnen – ein kühnes Experiment, das britische Handelswege revolutionieren könnte.", False, None, None, 2, "Wirtschaft", "28.6"),
        (49, "Spukgeschichten rund um altes Kloster", "Ein verlassenes Kloster in Nordengland sorgt für Schlagzeilen, nachdem mehrere Wanderer von unerklärlichen Erscheinungen berichteten.", False, None, None, 1, "Gesellschaft", "1.7"),
        (50, "Straßenbahnprojekt in Birmingham genehmigt", "Die Stadtverwaltung hat den Bau einer dampfbetriebenen Straßenbahn genehmigt. " "Die ersten Linien sollen innerhalb der nächsten fünf Jahre entstehen.", True, None, None, 3, "Wirtschaft", "4.7"),
        (51, "Mechanischer Butler sorgt für Aufsehen", "Ein Erfinder in London hat einen mechanischen Butler vorgestellt, der einfache Aufgaben erledigen kann. " "Die Aristokratie zeigt großes Interesse an der neuartigen Technik.", False, None, None, 3, "Wirtschaft", "8.7"),
        (52, "Hochwasser in Wales", "Heftige Regenfälle haben in Teilen von Wales zu Überschwemmungen geführt. " "Viele Bewohner mussten ihre Häuser verlassen.", True, None, None, 2, "Gesellschaft", "12.7"),
        (53, "Geheimnisvolles Artefakt in Londoner Keller gefunden", "Bei Renovierungsarbeiten in einem alten Stadthaus wurde ein versiegeltes Metallgehäuse entdeckt, dessen Ursprung unklar ist.", False, None, None, 2, "Wirtschaft", "15.7"),

        (54, "Explosion in Londoner Chemiefabrik", 
        "Eine gewaltige Explosion erschütterte das Industrieviertel von London. "
        "In einer Chemiefabrik kam es zu einem Unfall, der mehrere Arbeiter das Leben kostete. Ermittlungen laufen.",
        True, None, None, 3, "Einbruch", "01.02"),
        (55, "Skandal: Adliger wegen Spielschulden enteignet", 
        "Ein hochrangiger Adliger verlor sein gesamtes Vermögen durch exzessive Glücksspiele. "
        "Sein Anwesen wurde beschlagnahmt, und seine Familie steht vor dem finanziellen Ruin.",
        False, None, None, 2, "Gesellschaft", "02.09"),
        (56, "Neue Kanalverbindung zwischen London und Bristol geplant", 
        "Die Regierung kündigte ein ehrgeiziges Infrastrukturprojekt an: "
        "Ein neuer Kanal soll die Handelsrouten zwischen London und Bristol verkürzen.",
        True, None, None, 3, "Wirtschaft", None),
        (57, "Wagenrennen in Hyde Park begeistert Zuschauer", 
        "Ein illegales Pferderennen zog zahlreiche Zuschauer in den Hyde Park. "
        "Die Polizei ließ die Teilnehmer laufen, doch die Behörden erwägen härtere Maßnahmen gegen solche Veranstaltungen.",
        False, None, None, 2, "Veranstaltung", None),
        (58, "Neues Dampfschiff überquert den Ärmelkanal", 
        "Ein neu entwickeltes Dampfschiff bewältigte erstmals die Überquerung des Ärmelkanals in Rekordzeit. "
        "Experten sehen darin eine Revolution für den internationalen Handel.",
        False, None, None, 3, "Wirtschaft", None),
        (59, "Großes Feuer in Edinburghs Altstadt", 
        "Ein verheerendes Feuer zerstörte mehrere historische Gebäude in Edinburghs Altstadt. "
        "Die Feuerwehr kämpfte stundenlang gegen die Flammen.",
        True, None, None, 3, "Einbruch", None),
        (60, "Geheimbund in London entdeckt?", 
        "In einem Kellergewölbe wurden geheime Treffen einer mysteriösen Organisation beobachtet. "
        "Die Polizei untersucht mögliche Verbindungen zu politischen Unruhen.",
        True, None, None, 2, "Infos um die Königsfamilie", None),
        (61, "Erster Wetterballon erfolgreich gestartet", 
        "Wissenschaftler in Cambridge ließen einen Wetterballon steigen, "
        "um Windströme in höheren Luftschichten zu erforschen – ein bahnbrechender Fortschritt für die Meteorologie.",
        False, None, None, 2, "Wirtschaft", None),
        (62, "Berüchtigter Dieb in London gefasst", 
        "Nach monatelanger Flucht wurde der berüchtigte Juwelendieb 'Der Schatten von Soho' endlich gefasst. "
        "Er soll für zahlreiche spektakuläre Diebstähle verantwortlich sein.",
        True, None, None, 3, "Einbruch", None),
        (63, "Neues Waisenhaus in Liverpool eröffnet", 
        "Dank großzügiger Spenden konnte in Liverpool ein neues Waisenhaus errichtet werden. "
        "Die Einrichtung soll obdachlosen Kindern eine Zukunft bieten.",
        False, None, None, 2, "Gesellschaft", None),
        (64, "Brutaler Straßenkampf in Manchester", 
        "Zwei rivalisierende Banden lieferten sich eine blutige Auseinandersetzung in den Straßen von Manchester. "
        "Mehrere Personen wurden verletzt, die Polizei greift hart durch.",
        True, None, None, 3, "Einbruch", None),
        (65, "Berühmter Uhrmacher präsentiert revolutionäre Taschenuhr", 
        "Ein Uhrmacher aus London stellte eine neue Taschenuhr mit selbstaufziehendem Mechanismus vor. "
        "Dieses Meisterwerk könnte die Art, wie wir Zeit messen, für immer verändern.",
        False, None, None, 3, "Wirtschaft", None),
        (66, "Königliche Yacht gerät in Sturm", 
        "Die königliche Familie entging nur knapp einer Katastrophe, als ihre Yacht in einen heftigen Sturm geriet. "
        "Glücklicherweise konnte das Schiff sicher anlegen.",
        True, None, None, 3, "Infos um die Königsfamilie", None),
        (67, "Neues Theaterstück feiert Premiere in London", 
        "Das neueste Stück des berühmten Dramatikers Edward Harrington feierte eine umjubelte Premiere "
        "und könnte die Theaterszene revolutionieren.",
        False, None, None, 2, "Veranstaltung", None),
        (68, "Geheimes Treffen von Industriellen in Birmingham", 
        "Ein exklusives Treffen einflussreicher Fabrikbesitzer sorgt für Spekulationen über ein mögliches Kartellabkommen.",
        True, None, None, 2, "Wirtschaft", None),
        (69, "Schneesturm legt Nordengland lahm", 
        "Ein unerwarteter Schneesturm führte zu schweren Verkehrsbehinderungen und Stromausfällen in ganz Nordengland.",
        True, None, None, 3, "Infos um die Königsfamilie", None),
        (70, "Doppelte Hochzeit in königlicher Familie", 
        "Gleich zwei Mitglieder der königlichen Familie gaben sich am selben Tag das Ja-Wort. "
        "Ganz London feierte die prachtvollen Zeremonien.",
        False, None, None, 2, "Infos um die Königsfamilie", None),
        (71, "Junge Wissenschaftlerin entdeckt neues Element", 
        "Eine brillante Forscherin behauptet, ein bislang unbekanntes chemisches Element isoliert zu haben. "
        "Falls sich dies bestätigt, könnte es bahnbrechende Auswirkungen haben.",
        False, None, None, 3, "Wirtschaft", None),
        (72, "Riesiger Wal vor der Küste von Brighton gesichtet", 
        "Ein gigantischer Wal wurde von Fischern vor der Küste gesichtet. "
        "Experten rätseln, ob es sich um eine seltene Spezies handelt.",
        False, None, None, 2, "Infos um die Königsfamilie", None),
        (73, "Hochrangiger Diplomat unter Spionageverdacht", 
        "Ein hochrangiger Diplomat wird beschuldigt, geheime Informationen an ausländische Mächte weitergegeben zu haben. "
        "Die Ermittlungen laufen auf Hochtouren.",
        True, None, None, 3, "Infos um die Königsfamilie", None),
        (74, "Wunderkind begeistert London mit Klavierkonzert", 
        "Ein erst zehnjähriger Pianist sorgt mit seinem außergewöhnlichen Talent für Aufsehen in der Londoner Musikszene.",
        False, None, None, 2, "Veranstaltung", None),
        (75, "Seltene Orchidee in Schottland entdeckt", 
        "Botaniker jubeln: Eine äußerst seltene Orchideenart wurde in den schottischen Highlands entdeckt.",
        False, None, None, 1, "Infos um die Königsfamilie", None),
        (76, "Neuer Kanal unter der Themse geplant", 
        "Die Stadtverwaltung plant ein ehrgeiziges Bauprojekt: Einen Tunnel unter der Themse, um den Verkehr zu entlasten.",
        True, None, None, 3, "Wirtschaft", None),
        (77, "Wissenschaftler warnt vor Klimaveränderungen", 
        "Ein angesehener Forscher behauptet, dass der Mensch das Klima beeinflusst. "
        "Seine Theorien werden kontrovers diskutiert.",
        False, None, None, 2, "Wirtschaft", None),
        (78, "Revolutionäre Medizin gegen Lungenkrankheiten", 
        "Ärzte berichten über vielversprechende Fortschritte in der Behandlung von Lungenkrankheiten durch eine neue Heilmethode.",
        False, None, None, 3, "Wirtschaft", None),
        (79, "Einbruch in der Bank of England erschüttert London", 
         "In der Nacht von Dienstag auf Mittwoch drangen unbekannte Täter in die Bank of England ein. Der Tresor wurde mit Sprengstoff geöffnet, "
         "und mehrere wertvolle Sammlungen wurden gestohlen. Augenzeugen berichten von maskierten Tätern, die in einer Pferdekutsche flüchteten.",
         True, None, None, 3, "Einbruch", None),
        
        (80, "Zweiter Bankraub in London – Polizei tappt im Dunkeln", 
         "Wenige Tage nach dem spektakulären Bankraub wurden zwei weitere Banken im Stadtzentrum ausgeraubt. Die Polizei steht vor einem Rätsel, da keine nennenswerten Spuren hinterlassen wurden.", 
         True, 79, None, 2, "Einbruch", None),
        
        (81, "Diebischer Fluch? Der dritte Banküberfall erschüttert die Stadt", 
         "In der Nacht zum Sonntag ereignete sich der dritte Bankraub in London innerhalb von zwei Wochen. Diesmal wurde die Royal Bank von England getroffen. Der Täter hinterließ eine mysteriöse Nachricht.", 
         True, 80, None, 3, "Einbruch", None),
        
        # Storyline 2: Demonstrationen gegen Arbeiterrechte
        (82, "Massive Arbeiterproteste in Manchester", 
         "Tausende Arbeiter versammelten sich auf dem Marktplatz in Manchester, um gegen die miserablen Arbeitsbedingungen in den Textilfabriken zu protestieren. Einige berichteten von gewaltsamen Zusammenstößen mit der Polizei.", 
         True, None, None, 3, "Demonstrationen", "26.03"),
        
        (83, "Forderungen nach besseren Arbeitsbedingungen werden laut", 
         "Die Demonstranten fordern die Einführung von Arbeitszeitbegrenzungen und besseren Löhnen. Es gab Spekulationen, dass einige der Arbeiter von politischen Aktivisten beeinflusst wurden.", 
         True, 82, None, 2, "Demonstrationen", "29.03"),
        
        (84, "Protest eskaliert: Arbeiter fordern den Rücktritt von Fabrikbesitzern", 
         "Die Proteste in Manchester eskalierten, als Arbeiter begannen, die Türen der Fabriken zu blockieren. Es gibt Berichte über vereitelte Verhandlungen mit den Fabrikbesitzern.", 
         True, 83, None, 3, "Demonstrationen", "01.04"),
        
        # Storyline 3: Königliche Ereignisse
        (85, "Die Königin erwartet ein weiteres Kind!", 
         "Mit Freude wurde bekannt gegeben, dass die Königin erneut schwanger ist. Das königliche Paar erwartet sein fünftes Kind. Palastangestellte bestätigen, dass die Schwangerschaft gut verläuft.", 
         True, None, None, 3, "Infos um die Königsfamilie", "11.04"),
        
        (86, "Königlicher Nachwuchs: Junge Prinzessin erwartet", 
         "Es wurde bestätigt, dass das königliche Kind ein Mädchen wird. Die Bevölkerung fiebert bereits dem Moment entgegen, in dem die kleine Prinzessin das Licht der Welt erblickt.", 
         True, 85, None, 2, "Infos um die Königsfamilie", "12.04"),
        
        (87, "Geburt der Prinzessin – Land feiert", 
         "Heute Morgen wurde die Prinzessin in den königlichen Palast geboren. Tausende Menschen versammelten sich, um den königlichen Nachwuchs zu feiern. Das Land ist in festlicher Stimmung.", 
         True, 86, None, 3, "Infos um die Königsfamilie", "14.04"),
        
        # Storyline 4: Jahrmarkt in York
        (88, "Der Jahrmarkt in York öffnet seine Tore", 
         "Der traditionelle Jahrmarkt in York wurde heute mit einem großen Festzug eröffnet. Hunderte von Besuchern strömten zu den Ständen, um sich den bunten Treiben hinzugeben.", 
         True, None, None, 2, "Veranstaltung", "18.04"),
        
        (89, "Über 100.000 Besucher auf dem Jahrmarkt erwartet", 
         "Der Jahrmarkt in York hat einen Rekordbesuch verzeichnet, und es wird erwartet, dass mehr als 100.000 Menschen die Veranstaltung besuchen. Die Atmosphäre ist voller Energie, und die Schausteller berichten von ausgezeichneten Geschäften.", 
         True, 88, None, 3, "Veranstaltung", "22.04"),
        
        (90, "Jahrmarkt in York endet mit großem Feuerwerk", 
         "Der Jahrmarkt in York ging gestern mit einem spektakulären Feuerwerk zu Ende. Es war das größte Feuerwerk, das die Stadt je gesehen hat, und die Teilnehmer waren begeistert.", 
         True, 89, None, 3, "Veranstaltung", "24.04"),
        (79, "Wirtschaftsmanipulation in London – Verdacht auf geheime Verschwörung",
        "In London wird derzeit eine groß angelegte Wirtschaftskrise untersucht, die möglicherweise auf geheimen Verschwörungen innerhalb der Finanzwelt basiert. Experten sprechen von einer gezielten Manipulation des Marktes durch unbekannte Akteure.", 
        True, None, None, 3, "Wirtschaft", "26.04"),

        (80, "Gerüchte um mysteriösen Einbruch in Londons größte Bank",
        "In der vergangenen Nacht ereignete sich ein spektakulärer Einbruch in die größte Bank Londons. Die Täter entwendeten nicht nur Geld, sondern auch vertrauliche Dokumente, die nun von der Polizei untersucht werden. Experten vermuten, dass dies Teil einer größeren Verschwörung ist.", 
        True, 79, 2, 2, "Einbruch", "27.04"),

        (81, "Politische Demonstrationen gegen Finanzelite nehmen zu",
        "Die Unzufriedenheit mit der Wirtschaftssituation wächst. Tausende versammelten sich heute vor dem Parlament und forderten Reformen in der Finanzwelt. Aktivisten behaupten, dass eine geheime Verschwörung der Finanzelite für die Krise verantwortlich sei.",
        True, 80, 3, 3, "Demonstrationen", "28.04"),

        (82, "Polizei verhaftet verdächtige Banker in Zusammenhang mit Verschwörung",
        "Nach intensiven Ermittlungen wurden mehrere Banker wegen ihrer mutmaßlichen Beteiligung an der geheimen Verschwörung verhaftet. Die Polizei ermittelt weiter, ob sie Teil eines internationalen Netzwerks sind, das die Finanzmärkte manipuliert.",
        True, 81, 2, 3, "Wirtschaft", "07.05"),

        (83, "Enthüllung eines Skandals – Verantwortliche der Finanzwelt unter Verdacht",
        "Die Ermittlungen haben nun bestätigt, dass eine Gruppe von führenden Finanzberatern hinter der Verschwörung steckt. Die Öffentlichkeit ist erschüttert, und viele fordern eine vollständige Offenlegung der Verantwortlichen.",
        True, 82, 3, 3, "Wirtschaft", "08.05"),

        # Storyline 2: Die königliche Tragödie
        (84, "Königliche Tragödie erschüttert das Land",
        "Das Land ist in Trauer, nachdem bekannt wurde, dass der königliche Prinz auf mysteriöse Weise verstorben ist. Die genauen Umstände seines Todes sind noch unbekannt, doch der Palast spricht von einer persönlichen Tragödie.", 
        True, None, None, 3, "Infos um die Königsfamilie", "25.03"),

        (85, "Verschwörungstheorien über den Tod des Prinzen breiten sich aus",
        "In den Straßen Londons kursieren die wildesten Theorien über den Tod des Prinzen. Einige behaupten, es handele sich um einen Mord, während andere glauben, dass dunkle Mächte im Spiel sind. Die Polizei fordert die Bevölkerung zu Ruhe und Geduld auf.", 
        True, 84, 2, 2, "Infos um die Königsfamilie", "26.03"),

        (86, "Skandal im Königshaus – Verdacht auf Mordanschlag",
        "Es gibt immer mehr Hinweise darauf, dass der Tod des Prinzen kein Unfall war, sondern ein gezielter Mordanschlag. Die königliche Familie hat angekündigt, alles zu tun, um die Wahrheit ans Licht zu bringen.", 
        True, 85, 3, 3, "Gesellschaft", "27.03"),

        (87, "Einbruch im Palast – Wichtige Beweise verschwinden",
        "Wenige Tage nach dem Tod des Prinzen kam es zu einem Einbruch im Palast. Einbrüche dieser Art sind sehr selten, und die Polizei vermutet, dass die Täter Beweise im Zusammenhang mit dem Tod des Prinzen gesucht haben.",
        True, 86, 2, 3, "Einbruch", "28.03"),

        (88, "Königliche Familie fordert Aufklärung und Gerechtigkeit",
        "Der König hat öffentlich erklärt, dass er alles tun wird, um den Mord an seinem Sohn aufzuklären. Der Palast ist nun in ständiger Angst vor weiteren Angriffen.", 
        True, 87, 3, 3, "Infos um die Königsfamilie", "29.03"),

        # Storyline 3: Der Aufstieg des Unternehmers
        (89, "Ein Unternehmer revolutioniert die Eisenbahnindustrie",
        "Der Unternehmer Charles W. Jackson hat heute eine neue Eisenbahnstrecke eröffnet, die Londons Handel mit dem Norden erheblich beschleunigen soll. Experten sind sich einig, dass dies der Beginn einer neuen Ära im Transportwesen ist.", 
        True, None, None, 3, "Wirtschaft", "01.04"),

        (90, "Jacksons neue Strecken verzeichnen enorme Besucherzahlen",
        "Die neue Eisenbahnlinie hat bereits in den ersten Tagen Hunderttausende von Reisenden angezogen. Die Gesellschaft des Unternehmers expandiert weiter, und Jackson wird als der nächste Großindustrielle gefeiert.", 
        True, 89, 2, 2, "Wirtschaft", "02.04"),

        (91, "Eröffnung des jährlichen Eisenbahn-Festivals in London",
        "London feiert das jährliche Eisenbahn-Festival. Diesmal wird Charles W. Jackson selbst anwesend sein, um seine Innovationen vorzustellen und zu zeigen, wie seine Eisenbahnen das Leben der Bevölkerung verändert haben.", 
        True, 90, 3, 3, "Veranstaltung", "04.04"),

        (92, "Kritik an Jacksons Geschäftspraktiken – Sind seine Methoden ethisch?",
        "Trotz des Erfolges des Unternehmers gibt es Stimmen, die Jacksons Geschäftspraktiken als unethisch bezeichnen. Einige behaupten, er habe seine Arbeiter schlecht behandelt, um den Profit zu maximieren.", 
        True, 91, 2, 2, "Wirtschaft", "06.04"),

        (93, "Jacksons Eisenbahn-Imperium wächst weiter – Die Zukunft der Industrie",
        "Mit der Eröffnung weiterer Strecken und dem Ausbau seines Imperiums zeigt Jackson keine Anzeichen von Stagnation. Experten sind sich einig, dass er die Zukunft der Eisenbahnindustrie maßgeblich prägen wird.", 
        True, 92, 3, 3, "Wirtschaft", "07.04"),
        (94, "Neujahrsansprache des Königs", 
        "Der König von Großbritannien hält seine jährliche Neujahrsansprache, in der er auf das vergangene Jahr zurückblickt und die Ziele der Monarchie für das kommende Jahr darlegt.", 
        True, None, None, 3, "Infos um die Königsfamilie", "01.01"),

        (95, "Faschingsumzug in London", 
        "London feiert den Faschingsumzug mit prachtvollen Kostümen und Umzügen durch die Straßen der City. Besonders beliebt sind die Maskenbälle in den gehobenen Gesellschaften.", 
        True, None, None, 3, "Feste", "15.02"),

        (96, "Frühjahrsmarkt in Covent Garden", 
        "Der jährliche Frühjahrsmarkt in Covent Garden öffnet seine Tore. Händler aus ganz England bringen ihre Waren, von frischen Blumen bis hin zu handgefertigten Produkten.", 
        True, None, None, 3, "Veranstaltung", "01.04"),

        (97, "Eröffnung der Londoner Weltausstellung", 
        "Die Londoner Weltausstellung öffnet ihre Tore und präsentiert die neuesten technologischen Fortschritte, darunter die ersten Dampfmaschinen und innovative Maschinenbaukunst.", 
        True, None, None, 3, "Wirtschaft", "01.05"),

        (98, "Eröffnung der neuen Eisenbahnstrecke von London nach Brighton", 
        "Mit großer Begeisterung wird die neue Eisenbahnverbindung zwischen London und Brighton eröffnet. Die Strecke verkürzt die Reisezeit erheblich und revolutioniert den Tourismus an der Südküste.", 
        True, None, None, 3, "Wirtschaft", "15.06"),

        (99, "Prozession zum Erntedankfest", 
        "Eine große Prozession zum Erntedankfest findet in der St. Paul’s Cathedral statt. Bauern und Handwerker bringen ihre Gaben dar, und die Königin nimmt an den Feierlichkeiten teil.", 
        True, None, None, 3, "Feste", "15.10"),

        (100, "Königliche Hochzeit im Buckingham Palace", 
        "Das ganze Land schaut auf die königliche Hochzeit von Prinz Albert und Königin Victoria. Die Feierlichkeiten umfassen eine prächtige Prozession und ein Festmahl im Buckingham Palace.", 
        True, None, None, 3, "Infos um die Königsfamilie", "10.02"),

        (101, "Jahrmarkt in East End", 
        "Der jährliche Jahrmarkt im East End von London lockt mit Karussells, Ständen für handgefertigte Produkte und traditionellen Spielen, die vor allem die ärmeren Bezirke Londons ansprechen.", 
        True, None, None, 3, "Veranstaltung", "20.07"),

        (102, "Charity-Ball im Mansion House", 
        "Im Mansion House wird ein wohltätiger Ball zugunsten der Arbeiter und Armen Londons veranstaltet. Die Spenden werden an lokale Waisenhäuser und Krankenhäuser verteilt.", 
        True, None, None, 3, "Gesellschaft", "05.11"),

        (103, "Königliche Jagd im Windsor Forest", 
        "Die königliche Familie trifft sich zur traditionellen Jagd im Windsor Forest. Mitglieder des Adels und prominente Gäste nehmen an diesem Ereignis teil.", 
        True, None, None, 3, "Infos um die Königsfamilie", "25.12"),

        (104, "Eröffnung des Crystal Palace", 
        "Der Crystal Palace wird eröffnet, ein Wahrzeichen der industriellen Revolution in London, das Ausstellungen und Weltausstellungen beherbergen soll.", 
        True, None, None, 3, "Wirtschaft", "01.06"),

        (105, "Londoner Pferderennen im Epsom Downs", 
        "Das berühmte Pferderennen in Epsom Downs zieht jährlich Tausende von Schaulustigen und Wettenden aus ganz England an.", 
        True, None, None, 3, "Veranstaltung", "02.06"),

        (106, "Eröffnung des Hyde Park Winter Wonderland", 
        "Im Winter wird das Hyde Park Winter Wonderland eröffnet, eine festliche Veranstaltung mit Eislaufbahnen, Karussells und einem großen Weihnachtsmarkt.", 
        True, None, None, 3, "Fest", "01.12"),

        (107, "Kunst- und Handwerksmarkt in Kensington", 
        "Der Kunst- und Handwerksmarkt in Kensington präsentiert lokale Künstler und Handwerker, die ihre einzigartigen Werke ausstellen und verkaufen.", 
        True, None, None, 3, "Veranstaltung", "10.09"),

        (108, "Gedenkfeier für den Sieg von Waterloo", 
        "Im Stadtzentrum von London findet eine große Gedenkfeier für den Sieg von Waterloo statt. Die Königsfamilie und hochrangige Militärs nehmen an der Parade teil.", 
        True, None, None, 3, "Infos um die Königsfamilie", "18.06"),

        (109, "Ritterturnier in Windsor", 
        "In Windsor wird ein traditionelles Ritterturnier abgehalten, bei dem die besten Ritter des Landes um den Titel des Königs kämpfen.", 
        True, None, None, 3, "Veranstaltung", "14.08"),

        (110, "Theateraufführung im West End", 
        "Eine neue Theateraufführung im West End von London sorgt für Begeisterung. Das Stück, das auf einem historischen Ereignis basiert, zieht viele Theaterliebhaber an.", 
        True, None, None, 3, "Veranstaltung", "15.11"),

        (111, "Märkte im Borough Market", 
        "Der Borough Market feiert den Beginn des Winterverkaufs mit frischen Produkten, warmen Speisen und handgefertigten Waren aus ganz Großbritannien.", 
        True, None, None, 3, "Veranstaltung", "01.12"),

        (112, "Arbeiterstreik in der Docklands", 
        "In den Docklands kommt es zu einem Arbeiterstreik, da die Hafenarbeiter höhere Löhne und bessere Arbeitsbedingungen fordern. Die Situation ist angespannt.", 
        True, None, None, 3, "Demonstrationen", "20.03"),

        (113, "Jubiläumsfeier der Queen Victoria", 
        "Die Bevölkerung feiert das 24-jährige Regierungsjubiläum von Königin Victoria mit einem großen Festzug und einer Reihe von Veranstaltungen in London.", 
        True, None, None, 3, "Infos um die Königsfamilie", "20.06"),

        (114, "Festival der Wissenschaft und Technik", 
        "Im Royal Albert Hall findet das jährliche Festival der Wissenschaft und Technik statt, bei dem die neuesten Innovationen der britischen Ingenieure und Wissenschaftler vorgestellt werden.", 
        True, None, None, 3, "Wirtschaft", "03.10"),

        (115, "Gala-Dinner im Savoy Hotel", 
        "Im berühmten Savoy Hotel findet ein exklusives Gala-Dinner statt, bei dem prominente Persönlichkeiten aus der britischen Gesellschaft und Kunstszene anwesend sind.", 
        True, None, None, 3, "Gesellschaft", "15.07"),

        (116, "Frühjahrsreise nach Brighton", 
        "Die Hochburg der britischen Sommergäste – Brighton – öffnet seine Tore und lädt zu einem exklusiven Frühjahrsurlaub ein, mit vielen Unterhaltungsmöglichkeiten entlang des Strandes.", 
        True, None, None, 3, "Veranstaltung", "10.05"),

        (117, "Theaterstück im Globe Theatre", 
        "Im Globe Theatre wird ein neues Shakespeare-Stück aufgeführt, das die Zuschauermengen in London fesselt und begeistert.", 
        True, None, None, 3, "Veranstaltung", "15.02"),

        (118, "Hochzeit im Westminster Abbey", 
        "Im Westminster Abbey wird eine königliche Hochzeit gefeiert. Die ganze Nation schaut zu, wenn das frisch vermählte Paar ihren Eheversprechen ablegt.", 
        True, None, None, 3, "Infos um die Königsfamilie", "01.05"),

        (119, "Eröffnung des Londoner Zoo", 
        "Der Londoner Zoo wird eröffnet und zieht viele neugierige Besucher an. Es ist der erste Zoo der Welt, der Tiere aus allen Teilen der Erde zeigt.", 
        True, None, None, 3, "Veranstaltung", "02.04"),

        (120, "Kunstgalerie im Tate Modern", 
        "Das Tate Modern eröffnet eine neue Ausstellung mit Werken aus der viktorianischen Zeit, die das künstlerische Erbe Englands ehrt.", 
        True, None, None, 3, "Veranstaltung", "10.08"),
        (121, "Erste erfolgreiche Dampflokfahrt von London nach Edinburgh", 
        "Die erste Dampflokfahrt von London nach Edinburgh war ein großer Erfolg. Die Reise, die Stunden schneller war als erwartet, ebnet den Weg für den interstädtischen Verkehr.", 
        True, None, None, 3, "Wirtschaft", "12.05"),

        (122, "Der erste britische Flugzeugtest in Windsor", 
        "Ein mutiger Ingenieur aus Manchester hat in Windsor erfolgreich den ersten Flugzeugtest in Großbritannien durchgeführt. Die britische Luftfahrt hat jetzt einen ersten Fuß in die Geschichte gesetzt.", 
        True, None, None, 3, "Wirtschaft", "01.07"),

        (123, "Gerüchte über die Entführung des Duke of Cornwall", 
        "Gerüchte über die Entführung des Duke of Cornwall verbreiten sich in London. Während keine Bestätigung vorliegt, ist die Stadt in Aufruhr. Die Polizei bittet um Zeugenaussagen.", 
        True, None, None, 3, "Infos um die Königsfamilie", "23.04"),

        (124, "Skandal im Parlament: Abgeordneter im Skandal um Korruption verwickelt", 
        "Ein hochrangiger Abgeordneter des britischen Parlaments ist im Zusammenhang mit einem großen Korruptionsskandal festgenommen worden. Die Bevölkerung ist entsetzt, und die politische Szene erschüttert.", 
        True, None, None, 3, "Politik", "10.06"),

        (125, "Erste öffentliche Lesung von Charles Dickens' neuestem Werk", 
        "Charles Dickens gibt die erste öffentliche Lesung seines neuesten Romans. Die Veranstaltung ist ein riesiger Erfolg, und Tausende strömen in das Theater, um den Meister des viktorianischen Romans zu hören.", 
        True, None, None, 3, "Gesellschaft", "01.10"),

        (126, "Geheime Gesellschaft plant Revolution in den Straßen Londons", 
        "Ein geheimes Treffen einer revolutionären Gesellschaft in den düsteren Gassen Londons wirft Schatten auf die politische Stabilität des Landes. Berichte deuten auf mögliche Umstürze hin.", 
        True, None, None, 2, "Demonstrationen", "15.08"),

        (127, "Weltrekord im Bau der längsten Eisenbahnbrücke", 
        "Ingenieure in Großbritannien haben einen Weltrekord im Bau der längsten Eisenbahnbrücke aufgestellt. Dies ist ein monumentaler Erfolg der britischen Ingenieurskunst.", 
        True, None, None, 3, "Wirtschaft", "12.03"),

        (128, "Ungeklärter Mordfall in den dunklen Gassen von Whitechapel", 
        "Die Mordserie in Whitechapel geht weiter. Ein neuer, ungeklärter Mordfall hat die Öffentlichkeit erneut erschüttert und die Polizei steht unter Druck, den Fall zu lösen.", 
        True, None, None, 3, "Einbruch", "28.10"),

        (129, "Königliche Reise nach Irland führt zu Aufruhr", 
        "Königin Victoria und Prinz Albert reisen nach Irland. Währenddessen kommt es zu Protesten und Aufständen, als die Bevölkerung sich gegen die britische Herrschaft erhebt.", 
        True, None, None, 3, "Infos um die Königsfamilie", "05.06"),

        (130, "Große Ausstellung für viktorianische Kunst in London", 
        "Eine riesige Ausstellung für viktorianische Kunst wird im British Museum eröffnet. Die Ausstellung zeigt die besten Werke der viktorianischen Künstler, darunter Malerei, Skulpturen und Fotografie.", 
        True, None, None, 3, "Veranstaltung", "20.11"),

        (131, "Kritiker behaupten, der Big Ben sei nicht mehr zuverlässig", 
        "In einer scharfen Kritik haben führende Ingenieure behauptet, der Big Ben sei in seiner Funktionsweise nicht mehr zuverlässig und brauche dringend Reparaturen.", 
        True, None, None, 2, "Wirtschaft", "09.02"),

        (132, "Abgeordnete im Parlament fordern Reformen nach Arbeiterprotesten", 
        "Nach den jüngsten Arbeiterprotesten in London fordern Abgeordnete eine umfassende Reform des Arbeitsrechts, um die Lebensbedingungen der Arbeiterklasse zu verbessern.", 
        True, None, None, 3, "Demonstrationen", "15.05"),

        (133, "Zweite Weltausstellung öffnet in London", 
        "Die zweite Weltausstellung in London zieht Besucher aus aller Welt an und präsentiert die neuesten Erfindungen und Technologien der Industrie.", 
        True, None, None, 3, "Wirtschaft", "01.05"),

        (134, "Falkner der königlichen Familie gefangen in einem Sturm", 
        "Der Falkner der königlichen Familie ist während eines Ausflugs in den Yorkshire Dales in einem Sturm verloren gegangen. Glücklicherweise konnte er nach mehreren Tagen gerettet werden.", 
        True, None, None, 2, "Gesellschaft", "18.04"),

        (135, "Das erste elektrische Licht in London erleuchtet die Straßen", 
        "Das erste elektrische Licht wird an einer Straßenecke in London installiert. Das bedeutende Ereignis wird von einer großen Menschenmenge bestaunt.", 
        True, None, None, 3, "Wirtschaft", "25.12"),

        (136, "Neues Theaterstück von Oscar Wilde in London", 
        "Oscar Wilde präsentiert sein neuestes Theaterstück in London. Die Aufführung ist ein großer Erfolg und sorgt für Aufsehen in den Kreisen der Kunst- und Literaturwelt.", 
        True, None, None, 3, "Gesellschaft", "03.07"),

        (137, "Der erste Automobiltest in London endet in einem Unfall", 
        "Der erste Test eines Automobils in London endet mit einem spektakulären Unfall. Während das Fahrzeug einige Kilometer fuhr, konnte es seine Fahrt nicht erfolgreich fortsetzen.", 
        True, None, None, 3, "Wirtschaft", "15.08"),

        (138, "Berühmte Opernaufführung im Covent Garden", 
        "Eine neue, revolutionäre Oper wird im Covent Garden aufgeführt, die das Publikum begeistert und die britische Musikszene nachhaltig prägt.", 
        True, None, None, 3, "Veranstaltung", "20.09"),

        (139, "Geheime Korrespondenz der Regierung wird geleakt", 
        "Ein geheimes Dokument der Regierung, das wichtige politische Strategien und Allianzen betrifft, wird von einem unbekannten Informanten in die Presse geleakt.", 
        True, None, None, 2, "Politik", "22.03"),

        (140, "Führende britische Sozialreformer starten neue Bewegung", 
        "Eine Gruppe prominenter Sozialreformer startet eine neue Bewegung für die Rechte der Arbeiter und die Verbesserung der Lebensbedingungen der Armen.", 
        True, None, None, 3, "Demonstrationen", "15.05"),

        (141, "Das erste öffentliche Flugzeugrennen in London", 
        "In London findet das erste öffentliche Flugzeugrennen statt, bei dem die besten Piloten aus ganz Großbritannien gegeneinander antreten.", 
        True, None, None, 3, "Veranstaltung", "08.10"),

        (142, "Der erste öffentliche Wasserfall in einem Park", 
        "In einem neu angelegten Park in London wird der erste öffentliche Wasserfall installiert. Tausende Besucher kommen, um das spektakuläre Naturereignis zu bestaunen.", 
        True, None, None, 3, "Veranstaltung", "22.06"),

        (143, "Königin Victoria trifft sich mit ihren amerikanischen Verwandten", 
        "Königin Victoria trifft sich mit entfernten Verwandten aus Amerika, was zu zahlreichen Gerüchten und Spekulationen über politische Allianzen führt.", 
        True, None, None, 3, "Infos um die Königsfamilie", "10.11"),

        (144, "Erste elektrische Straßenbahn in London", 
        "London hat seine erste elektrische Straßenbahn auf die Straßen geschickt. Das Ereignis ist ein Meilenstein für die Verkehrsinfrastruktur der Stadt.", 
        True, None, None, 3, "Wirtschaft", "25.12"),

        (145, "Neuer Brückenbau über den Themse-Fluss", 
        "Eine neue Brücke über den Themse-Fluss wird eingeweiht, die den Verkehr zwischen East und West London erheblich verbessern soll.", 
        True, None, None, 3, "Wirtschaft", "05.05"),

        (146, "Das erste Flugzeug von London nach Paris startet", 
        "Der erste kommerzielle Flug von London nach Paris startet mit einer neuen, revolutionären Fluggesellschaft. Viele warten gespannt auf das Ergebnis.", 
        True, None, None, 3, "Wirtschaft", "14.09"),

        (147, "Ein mysteriöser Fremder im Tower of London", 
        "Ein mysteriöser Fremder wird in der Nähe des Tower of London gesehen, und Gerüchte über einen versuchten Einbruch oder einen geheimen Plan machen die Runde.", 
        True, None, None, 2, "Einbruch", "21.12"),

        (148, "Das erste Flugzeug, das in London landet", 
        "Ein Flugzeug aus Paris landet erfolgreich in London und eröffnet die Ära der internationalen Luftreisen.", 
        True, None, None, 3, "Wirtschaft", "18.10"),

        (149, "Erste elektrische U-Bahn in London", 
        "London feiert die Eröffnung seiner ersten elektrischen U-Bahn. Die Strecke verbindet die zentralen Bezirke und sorgt für eine enorme Erleichterung des Pendelverkehrs.", 
        True, None, None, 3, "Wirtschaft", "03.09"),

        (150, "Wiedereröffnung des British Museum nach Renovierung", 
        "Nach jahrelanger Renovierung öffnet das British Museum wieder seine Tore und wird mit neuen Ausstellungen und modernisierten Räumlichkeiten begrüßt.", 
        True, None, None, 3, "Veranstaltung", "21.12"),
        
        (151, "Kollision der Dampfschiffe auf der Themse", 
        "Heute Morgen ereignete sich eine dramatische Kollision zwischen zwei Dampfschiffen auf der Themse. Es wird vermutet, dass dichter Nebel und die Unkenntnis des neuen Navigationssystems zu dem Vorfall geführt haben.", 
        True, None, None, 2, "Wirtschaft", "17.07"),

        (152, "Verbotene Wissenschaft: Alchemist in den Londoner Docklands entdeckt", 
        "In den düsteren Docklands von London wurde ein Alchemist gefunden, der angeblich an einer alten Formel für die Erschaffung von Gold arbeitete. Die Polizei hat den Fall übernommen und alle Beweise beschlagnahmt.", 
        True, None, None, 3, "Einbruch", "22.08"),

        (153, "Seltsame Lichter über dem Tower von London", 
        "Gestern Nacht wurden mysteriöse Lichter über dem Tower of London gesehen. Ein örtlicher Astronom spricht von ungewöhnlichen Phänomenen, andere glauben an ein übernatürliches Ereignis.", 
        True, None, None, 2, "Gesellschaft", "03.11"),

        (154, "Gerüchte über den geheimen Plan von Lord Blackwood", 
        "Gerüchte aus der Oberschicht von London besagen, dass Lord Blackwood eine geheime Verschwörung plant, um die Krone zu stürzen. Obwohl noch nichts bestätigt wurde, sind die Gerüchte in den Salons der Stadt Gesprächsthema.", 
        True, None, None, 2, "Politik", "10.12"),

        (155, "Große Pferdeschau in Hyde Park endet mit unerklärlichem Vorfall", 
        "Die heute stattgefundene große Pferdeschau im Hyde Park endete mit einem mysteriösen Vorfall. Mehrere Pferde rannten wild durch die Menge, bevor sie plötzlich still standen und keiner konnte den Grund dafür erklären.", 
        True, None, None, 2, "Veranstaltung", "06.07"),

        (156, "Abgeordneter verschwindet nach geheimem Treffen mit unbekanntem Fremden", 
        "Ein hochrangiger Abgeordneter verschwand nach einem geheimen Treffen mit einem mysteriösen Fremden. Spekulationen über politische Geheimverhandlungen und mögliche Spionage machen die Runde.", 
        True, None, None, 3, "Politik", "14.09"),

        (157, "Geheime U-Bahn unter dem Buckingham Palast entdeckt", 
        "In den letzten Tagen wurden in der Nähe des Buckingham Palasts geheime Tunnel entdeckt. Es wird vermutet, dass die Tunnel während der Kriege genutzt wurden, aber ihre wahre Nutzung bleibt ein Rätsel.", 
        True, None, None, 3, "Einbruch", "30.10"),

        (158, "Unerklärliches Verschwinden von Kunstwerken im British Museum", 
        "Ungefähr ein Dutzend wertvoller Kunstwerke sind im British Museum verschwunden. Die Polizei hat Ermittlungen aufgenommen, doch es gibt noch keine Erklärung für das Verschwinden der Gemälde und Skulpturen.", 
        True, None, None, 3, "Einbruch", "11.06"),

        (159, "Erfindung eines Apparats zur Vorhersage von Naturkatastrophen", 
        "Ein Ingenieur in London behauptet, eine Vorrichtung erfunden zu haben, die Naturkatastrophen wie Erdbeben und Stürme vorhersagen kann. Die wissenschaftliche Welt ist geteilt in ihrer Bewertung dieses angeblichen Durchbruchs.", 
        True, None, None, 3, "Wirtschaft", "20.05"),

        (160, "Hochzeit des Jahrhunderts: Prinzessin Victoria heiratet Herzog von Cambridge", 
        "Heute fand die prachtvolle Hochzeit von Prinzessin Victoria und dem Herzog von Cambridge statt. Die königliche Familie und das gesamte Land jubelten diesem bedeutenden Ereignis zu.", 
        True, None, None, 3, "Infos um die Königsfamilie", "15.07"),

        (161, "Berühmte Londoner Künstler veranstalten eine geheime Kunstausstellung", 
        "Ein geheimes Treffen der führenden Londoner Künstler fand heute statt, bei dem neue Werke präsentiert wurden, die nicht der Öffentlichkeit zugänglich gemacht wurden. Die Werke sollen in den kommenden Wochen veröffentlicht werden.", 
        True, None, None, 3, "Gesellschaft", "02.11"),

        (162, "Götterdämmerung im Tower: Geheimnisvolle Inschrift gefunden", 
        "Im Tower of London wurde eine geheimnisvolle Inschrift entdeckt, die von einer längst vergessenen Kulturschicht zu stammen scheint. Einige Historiker sind überzeugt, dass es sich um eine Botschaft aus der Zukunft handelt.", 
        True, None, None, 2, "Einbruch", "21.08"),

        (163, "Zeppelin von Frankfurt nach London erfolgreich", 
        "Der erste Zeppelin, der von Frankfurt nach London flog, landete heute erfolgreich. Der Flug, der über den Ärmelkanal führte, war ein historischer Meilenstein für die Luftfahrt und wird als Beginn des Zeppelin-Zeitalters gefeiert.", 
        True, None, None, 3, "Wirtschaft", "03.10"),

        (164, "Gefährlicher Spuk im alten Londoner Theater", 
        "Das historische Victoria-Theater in London steht im Mittelpunkt eines mysteriösen Vorfalls. Zahlreiche Berichte von Schauspielern und Zuschauern über seltsame Vorkommnisse und Erscheinungen sind zu einer lokalen Sensation geworden.", 
        True, None, None, 2, "Gesellschaft", "01.12"),

        (165, "Erste Expedition in die Tiefen des Loch Ness", 
        "Ein Wissenschaftler aus London hat die erste Expedition zu den geheimen Tiefen des Loch Ness in Schottland geleitet. Die Expedition soll neue Erkenntnisse über die mysteriösen Erscheinungen im See bringen.", 
        True, None, None, 2, "Veranstaltung", "27.07"),

        (166, "Die Rückkehr des wahren Königsmantels von König Arthur", 
        "Nach jahrhundertelangen Spekulationen und Legenden ist der wahre Königsmantel von König Arthur in einem geheimen Ort in Cornwall wiederentdeckt worden. Experten vermuten, dass der Mantel magische Eigenschaften besitzen könnte.", 
        True, None, None, 3, "Infos um die Königsfamilie", "18.09"),

        (167, "Das Verschwinden der königlichen Juwelen: Die Ermittlungen beginnen", 
        "Die wertvollen königlichen Juwelen sind unter mysteriösen Umständen verschwunden. Die Polizei geht von einem ausgeklügelten Diebstahl aus, doch der wahre Täter bleibt unbekannt.", 
        True, None, None, 3, "Einbruch", "14.10"),

        (168, "Elektrisches Licht macht die Straßen Londons sicherer", 
        "Die Einführung von elektrischem Licht auf Londons Straßen hat die Sicherheit erheblich verbessert. Kriminalität in den Straßen ist gesunken, und die Londoner begrüßen die neue Beleuchtung als einen Fortschritt für ihre Stadt.", 
        True, None, None, 3, "Wirtschaft", "22.11"),

        (169, "Ungewöhnliche Wetterphänomene in der Themse-Region", 
        "Berichte über ein ungewöhnliches Wetterphänomen, bei dem es in der Themse-Region plötzlich zu einem extremen Temperaturabfall kam. Meteorologen sind ratlos, was dieses Ereignis ausgelöst haben könnte.", 
        True, None, None, 2, "Gesellschaft", "12.02"),

        (170, "Die erste elektrische Straßenbahn in Manchester fährt", 
        "Manchester hat seine erste elektrische Straßenbahn in Betrieb genommen. Die Eröffnung ist ein großer Schritt in die Zukunft des öffentlichen Verkehrs und wird von der Bevölkerung begeistert aufgenommen.", 
        True, None, None, 3, "Wirtschaft", "05.05"),

        (171, "Große Arktis-Expedition beginnt in London", 
        "Eine ehrgeizige Arktis-Expedition verlässt heute London, um neue Gebirgsketten und unbekannte Gebiete im hohen Norden zu erforschen. Die Expedition ist eines der ehrgeizigsten Unternehmen des Jahrhunderts.", 
        True, None, None, 3, "Veranstaltung", "22.03"),

        (172, "Dunkles Geheimnis im Buckingham Palast: Fremder unrechtmäßig eingedrungen", 
        "Ein Fremder wurde dabei erwischt, als er in Buckingham Palast einbrach. Warum dieser Mann in den Palast eindrang, bleibt ein ungelöstes Rätsel.", 
        True, None, None, 2, "Einbruch", "10.08"),

        (173, "Bühnenzauber: Weltpremiere der ersten Cinematographie-Show in London", 
        "Die erste öffentliche Vorführung eines Films fand heute in London statt. Das neue Medium der Cinematographie zieht Tausende von Zuschauern an, die von der neuen Art der Unterhaltung begeistert sind.", 
        True, None, None, 3, "Veranstaltung", "01.06"),

        (174, "Londoner Straßen von einem geheimen Mönch beherrscht", 
        "Ein geheimnisvoller Mönch hat in den Londoner Straßen seine Spuren hinterlassen. Er verbreitet mystische Lehren, und viele glauben, dass er eine geheime, alte Religion wiederbelebt.", 
        True, None, None, 2, "Demonstrationen", "03.09"),

        (175, "Ritterlicher Kampf auf dem königlichen Hof – Duell endet tragisch", 
        "Ein öffentliches Duell zwischen zwei Adligen auf dem königlichen Hof von London endet tragisch. Das blutige Ereignis wird von vielen als ein Symbol für die rückständigen Traditionen der britischen Aristokratie angesehen.", 
        True, None, None, 2, "Gesellschaft", "19.06"),

        (176, "Versuchter Anschlag auf die königliche Familie während einer Parade", 
        "Ein Anschlagsversuch auf die königliche Familie während einer Parade in London wurde glücklicherweise vereitelt. Die Täter wurden festgenommen, doch der Vorfall hat die öffentliche Meinung erschüttert.", 
        True, None, None, 3, "Einbruch", "27.12"),
        (177, "Der mysteriöse Fund im Tower von London", 
        "Bei Renovierungsarbeiten im Tower of London wurde ein geheimer Raum entdeckt. Darin fanden sich alte Manuskripte, die von einer längst vergessenen Wissenschaft sprechen, die den Menschen unsterblich machen soll.", 
        True, None, None, 3, "Einbruch", "10.02"),

        (178, "Ungewöhnliche Leuchtphänomene im Tower", 
        "Nachdem die geheimen Manuskripte im Tower von London entdeckt wurden, berichten mehrere Zeugen von mysteriösen Lichtern, die aus den Tiefen des Turms zu kommen scheinen. Einige glauben, die Entdeckung könnte zu einer übernatürlichen Entfaltung führen.", 
        True, 177, 3, 2, "Gesellschaft", "12.02"),

        (179, "Wissenschaftler führen geheimen Versuch durch", 
        "Ein Team von Wissenschaftlern hat in London ein Experiment gestartet, bei dem sie versuchen, die Geheimnisse der Manuskripte zu entschlüsseln. Gerüchten zufolge geht es dabei um eine neue Technologie zur Verlängerung des Lebens.", 
        True, 178, 5, 3, "Wirtschaft", "14.02"),

        # Storyline 2: "Politische Intrigen und eine gefährliche Verschwörung"
        (180, "Geheime Verschwörung gegen den Premierminister", 
        "Gerüchten zufolge hat eine Gruppe von hochrangigen Politikern eine Verschwörung gegen den Premierminister gesponnen, um die Regierung zu stürzen und das Land in eine neue politische Ära zu führen.", 
        True, None, None, 3, "Politik", "05.03"),

        (181, "Abgeordneter in den Skandal verwickelt", 
        "Ein bekannter Abgeordneter wurde dabei erwischt, wie er geheime Treffen mit ausländischen Diplomaten abhielt. Es wird vermutet, dass er Informationen über die Verschwörung gegen den Premierminister weitergab.", 
        True, 180, 2, 3, "Politik", "07.03"),

        (182, "Verschwörung aufgeflogen: Polizei entdeckt geheime Zelle", 
        "Die Polizei hat in einer verlassenen Fabrik in London eine geheime Zelle entdeckt, die von den Verschwörern genutzt wurde. Darin fanden sich detaillierte Pläne zur Umstürzung der Regierung und zur Manipulation der Wahlen.", 
        True, 181, 4, 3, "Einbruch", "09.03"),

        # Storyline 3: "Die Entdeckung eines sagenumwobenen Schatzes"
        (183, "Schatzkarte entdeckt: Der verlorene Schatz von King Arthur", 
        "Ein ehrgeiziger Archäologe in London hat eine Schatzkarte entdeckt, die angeblich zu einem verborgenen Schatz führen soll, der von König Arthur selbst vergraben wurde. Experten sind sich uneinig über die Echtheit der Karte.", 
        True, None, None, 2, "Wirtschaft", "02.04"),

        (184, "Die Suche nach dem Schatz beginnt", 
        "Eine Expedition wird auf den Weg geschickt, um den verlorenen Schatz von König Arthur zu finden. Die Reise führt sie durch abgelegene Gebirgspfade und geheimnisvolle Orte, die mit Legenden umwoben sind.", 
        True, 183, 5, 3, "Veranstaltung", "05.04"),

        (185, "Schatz gefunden: Das Geheimnis des Heiligen Grals", 
        "Nach monatelanger Suche haben die Expeditionsteilnehmer den Schatz gefunden – und entdecken ein altes Artefakt, das dem sagenumwobenen Heiligen Gral ähneln soll. Der Fund sorgt für weltweites Aufsehen und ist ein heiß diskutiertes Thema.", 
        True, 184, 3, 3, "Wirtschaft", "10.04"),

        # Storyline 4: "Das Geheimnis des verschwundenen Erfinders"
        (186, "Erfinder verschwindet unter mysteriösen Umständen", 
        "Der berühmte Ingenieur Sir Thomas Blackwell, bekannt für seine bahnbrechenden Erfindungen, ist spurlos verschwunden. Experten vermuten, dass er auf eine geheime Erfindung gestoßen ist, die die Menschheit revolutionieren könnte.", 
        True, None, None, 3, "Einbruch", "15.05"),

        (187, "Geheime Aufzeichnungen des Erfinders entdeckt", 
        "Ein Assistent von Sir Thomas Blackwell hat geheime Aufzeichnungen seines Mentors gefunden. Diese Dokumente beinhalten Entwürfe für ein Gerät, das angeblich die Luftfahrt revolutionieren könnte und möglicherweise eine Gefahr für die Regierung darstellt.", 
        True, 186, 5, 2, "Wirtschaft", "18.05"),

        (188, "Die Jagd nach Blackwells Erfindung", 
        "Die Entwürfe von Sir Thomas Blackwell haben eine Jagd nach seiner geheimen Erfindung ausgelöst. Zahlreiche Interessengruppen versuchen, die Technologie zu erlangen, während die Polizei die Ermittlungen fortsetzt, um zu verhindern, dass sie in die falschen Hände gerät.", 
        True, 187, 4, 3, "Einbruch", "21.05"),

        # Storyline 5: "Das verborgene Leben der Londoner Gesellschaft"
        (189, "Verborgene Welt der Londoner High Society", 
        "In den exklusiven Salons der Londoner Oberschicht kursieren Gerüchte über geheime Gesellschaften und das verborgene Leben der Mitglieder. Es heißt, einige der angesehensten Persönlichkeiten der Stadt seien in dunkle Machenschaften verwickelt.", 
        True, None, None, 2, "Gesellschaft", "20.06"),

        (190, "Einflussreiche Lady geht einem Geheimnis nach", 
        "Lady Margaret Hillingdon, bekannt für ihren Einfluss in der Londoner Gesellschaft, hat begonnen, die geheimen Gesellschaften zu untersuchen, von denen in den Salons gemunkelt wird. Ihre Nachforschungen könnten weitreichende Folgen haben.", 
        True, 189, 3, 2, "Gesellschaft", "25.06"),

        (191, "Skandal aufgedeckt: Die geheime Gesellschaft", 
        "Lady Margaret Hillingdon hat eine geheime Gesellschaft aufgedeckt, die in dunklen Ritualen und Machenschaften verstrickt ist. Der Skandal erschüttert das Fundament der Londoner Oberschicht und wird zu einem der größten gesellschaftlichen Skandale des Jahres.", 
        True, 190, 5, 3, "Gesellschaft", "30.06"),

        # Storyline 6: "Das unerklärliche Phänomen der Londoner Straßen"
        (192, "Unerklärliches Phänomen in den Straßen Londons", 
        "Ein seltsames Phänomen erschüttert London: In mehreren Stadtteilen werden nachts Lichter gesehen, die von einer unbekannten Quelle ausgehen. Einige behaupten, es sei ein übernatürliches Ereignis.", 
        True, None, None, 2, "Gesellschaft", "12.07"),

        (193, "Zeuge eines ungewöhnlichen Phänomens", 
        "Ein Augenzeuge berichtet von einem Vorfall, bei dem ein mysteriöses Licht über den Dächern von London schwebte. Die Polizei ist ratlos, aber viele glauben, dass es sich um ein bedeutendes Ereignis handelt.", 
        True, 192, 4, 2, "Gesellschaft", "14.07"),

        (194, "Erklärung für das Phänomen gefunden?", 
        "Nach umfangreichen Untersuchungen scheint es eine Erklärung für das Phänomen zu geben: Ein experimentelles Gerät zur Kommunikation über große Entfernungen könnte die Ursache gewesen sein. Doch einige zweifeln an dieser Erklärung.", 
        True, 193, 3, 2, "Wirtschaft", "17.07"),

        # Storyline 7: "Das mysteriöse Verschwinden eines berühmten Forschers"
        (195, "Berühmter Forscher verschwindet während einer Expedition", 
        "Der bekannte Botaniker Dr. Edmund Ralston, der für seine Expeditionen in abgelegene Gebirgsketten bekannt ist, ist bei seiner letzten Reise spurlos verschwunden.", 
        True, None, None, 3, "Veranstaltung", "22.08"),

        (196, "Letzte Nachricht des verschwundenen Forschers", 
        "Die letzte Nachricht, die von Dr. Edmund Ralston gesendet wurde, spricht von einem geheimen Fund in den Bergen von Wales. Es wird vermutet, dass er eine unbekannte Pflanze entdeckt hat, die medizinische Wunder bewirken könnte.", 
        True, 195, 3, 3, "Wirtschaft", "25.08"),

        (197, "Expedition zur Rettung von Dr. Ralston", 
        "Eine Rettungsmission wird in den Bergen von Wales gestartet, um Dr. Edmund Ralston zu finden. Doch die Expedition wird von einer Reihe seltsamer Ereignisse begleitet, die die Forscher erschüttern.", 
        True, 196, 4, 3, "Veranstaltung", "30.08"),
        
        (198, "Diamant des Herzogs aus London verschwunden", 
        "Der legendäre Diamant 'Königsblut', im Besitz des Herzogs von Windsor, wurde gestohlen. Berichten zufolge brach ein maskierter Dieb in das Anwesen ein, ohne Spuren zu hinterlassen. Die Polizei steht vor einem Rätsel.", 
        True, None, None, 3, "Einbruch", "11.10"),

        (199, "Gestohlener Diamant taucht in Paris auf", 
        "In einem exklusiven Pariser Auktionshaus tauchte der Diamant des Herzogs von Windsor auf. Experten sind sich sicher, dass es sich um den gestohlenen 'Königsblut'-Diamanten handelt. Doch wie gelangte er nach Paris?", 
        True, 198, 3, 3, "Einbruch", "14.10"),

        (200, "Die Jagd nach dem verschwundenen Diamanten", 
        "Die Polizei beginnt eine internationale Jagd, um den gestohlenen Diamanten zurückzuholen. Verdächtige sind ein kriminelles Netzwerk in London und Paris, das für seine geheimen Versteigerungen berüchtigt ist.", 
        True, 199, 4, 3, "Wirtschaft", "17.10"),

        # Storyline 2: "Die mysteriöse Entführung des Schriftstellers"
        (201, "Berühmter Schriftsteller in London entführt", 
        "Der gefeierte Schriftsteller Edmund Welles, bekannt für seine sozialkritischen Romane, wurde in der Nacht aus seiner Londoner Wohnung entführt. Erste Hinweise deuten auf eine Verschwörung innerhalb der literarischen Elite hin.", 
        True, None, None, 3, "Einbruch", "22.11"),

        (202, "Welles' Entführer fordern öffentliches Bekenntnis", 
        "Die Entführer von Edmund Welles haben Kontakt aufgenommen und fordern, dass der Schriftsteller ein öffentliches Bekenntnis zu seiner Unterstützung einer geheimen politischen Bewegung ablegt, um sein Leben zu retten.", 
        True, 201, 3, 3, "Gesellschaft", "24.11"),

        (203, "Welles' Entführer enttarnt: Ein Netzwerk von Politikern", 
        "Die Entführer von Edmund Welles werden als Teil eines politischen Netzwerks enttarnt, das darauf abzielt, die öffentliche Meinung zu manipulieren. Der Fall erschüttert das Vertrauen in die politische Landschaft Londons.", 
        True, 202, 5, 3, "Politik", "27.11"),

        # Storyline 3: "Das geheime Experiment der Oxford-Universität"
        (204, "Geheimes Experiment in Oxford", 
        "Berichten zufolge führt eine Gruppe von Wissenschaftlern an der Universität von Oxford ein geheimes Experiment durch, das den menschlichen Körper in der Lage versetzen soll, extreme Belastungen zu überstehen. Gerüchten zufolge könnten die Ergebnisse bahnbrechend sein.", 
        True, None, None, 2, "Wirtschaft", "05.12"),

        (205, "Forschungsprojekt von Oxford sorgt für Kontroversen", 
        "Das geheime Experiment an der Universität Oxford hat in der wissenschaftlichen Gemeinschaft für Aufsehen gesorgt. Einige Experten behaupten, dass die Ergebnisse die Grenzen der menschlichen Ethik überschreiten.", 
        True, 204, 3, 3, "Wirtschaft", "08.12"),

        (206, "Experten auf der ganzen Welt fordern ein Ende des Projekts", 
        "Weltweit rufen führende Wissenschaftler dazu auf, das geheime Experiment in Oxford sofort zu stoppen. Einige glauben, dass die Forscher gefährliche Grenzen überschreiten, die die Menschheit nicht überschreiten sollte.", 
        True, 205, 4, 3, "Gesellschaft", "10.12"),

        # Storyline 4: "Das Unglück auf dem Thames Dampfschiff"
        (207, "Katastrophe auf dem Thames Dampfschiff", 
        "Ein Dampfschiff auf der Themse ist bei dichtem Nebel gegen ein anderes Schiff gestoßen, was zu einer verheerenden Explosion führte. Zahlreiche Passagiere werden vermisst, und die Rettungsbemühungen laufen auf Hochtouren.", 
        True, None, None, 3, "Veranstaltung", "02.01"),

        (208, "Unfallursache des Dampfschiffs aufgedeckt", 
        "Die Ursache des tragischen Dampfschiffunglücks auf der Themse wird nun als technisches Versagen identifiziert. Gerüchten zufolge hatte das Dampfschiff in den letzten Wochen wiederholt technische Mängel, die jedoch nie behoben wurden.", 
        True, 207, 3, 3, "Wirtschaft", "05.01"),

        (209, "Erneute Untersuchung fordert Strafanzeige gegen Betreiber", 
        "Nach der Entdeckung, dass das Dampfschiff vor dem Unfall wiederholt unsicheren Zustand hatte, fordert die Öffentlichkeit nun, dass der Betreiber strafrechtlich verfolgt wird. Auch andere Schiffe im Betrieb müssen überprüft werden.", 
        True, 208, 4, 3, "Politik", "07.01"),

        # Storyline 5: "Das Geheimnis der verschwundenen Statue"
        (210, "Wertvolle Statue aus dem Britischen Museum verschwunden", 
        "Eine wertvolle antike Statue, die ursprünglich aus dem antiken Griechenland stammt, ist aus dem Britischen Museum verschwunden. Experten rätseln über das Verschwinden und vermuten ein internationales Kunstdiebstahlnetzwerk.", 
        True, None, None, 3, "Einbruch", "15.02"),

        (211, "Ein internationaler Kunstraub?", 
        "Berichten zufolge könnte der Diebstahl der Statue im Britischen Museum Teil eines internationalen Kunstraubnetzwerks sein. Erste Hinweise deuten darauf hin, dass mehrere prominente Kunstsammler in den Fall verwickelt sein könnten.", 
        True, 210, 4, 3, "Einbruch", "18.02"),

        (212, "Die Statue taucht in New York auf", 
        "Die gestohlene Statue aus dem Britischen Museum wurde in New York zum Verkauf angeboten. Die Polizei hat nun eine internationale Zusammenarbeit initiiert, um die Statue zurückzuholen und die Täter zu fassen.", 
        True, 211, 5, 3, "Einbruch", "20.02"),

        # Storyline 6: "Die mysteriösen Brände von Whitechapel"
        (213, "Mysteröse Brände in Whitechapel", 
        "In den letzten Wochen wurden mehrere Brände im Stadtteil Whitechapel gemeldet, die niemand erklären kann. Die Polizei vermutet Brandstiftung, doch die Ermittlungen haben bisher keine klaren Hinweise geliefert.", 
        True, None, None, 3, "Einbruch", "10.03"),

        (214, "Brandstiftung in Whitechapel aufgedeckt", 
        "Die Polizei hat Brandstifter in Whitechapel aufgedeckt, die scheinbar zufällige Gebäude in Brand setzen. Einige glauben, dass es sich um eine Gruppe handelt, die versucht, Angst in der Bevölkerung zu verbreiten.", 
        True, 213, 3, 3, "Einbruch", "12.03"),

        (215, "Die wahren Hintergründe der Brände aufgedeckt", 
        "Die Ermittlungen haben ergeben, dass die Brände in Whitechapel von einer geheimen Gesellschaft geplant wurden, die versuchte, die öffentliche Meinung zu beeinflussen. Der Skandal löst einen Sturm der Entrüstung aus.", 
        True, 214, 5, 3, "Politik", "15.03"),

        # Storyline 7: "Die rätselhafte Explosion im Londoner U-Bahn-System"
        (216, "Explosion erschüttert die Londoner U-Bahn", 
        "Eine gewaltige Explosion hat das Londoner U-Bahn-System erschüttert, wobei zahlreiche Menschen verletzt wurden. Noch ist unklar, ob es sich um einen terroristischen Anschlag oder einen technischen Defekt handelt.", 
        True, None, None, 3, "Veranstaltung", "22.04"),

        (217, "Explosion in der U-Bahn war kein Unfall", 
        "Nach den ersten Ermittlungen stellt sich heraus, dass die Explosion in der Londoner U-Bahn kein Unfall war. Es wird vermutet, dass ein technisches Gerät zur Sabotage eingesetzt wurde.", 
        True, 216, 3, 3, "Politik", "25.04"),

        (218, "Terroristische Zelle hinter U-Bahn-Explosion?", 
        "Die Polizei hat Hinweise auf eine terroristische Zelle gefunden, die möglicherweise hinter der U-Bahn-Explosion steckt. Der Fall wird nun von den Behörden auf höchster Ebene untersucht.", 
        True, 217, 5, 3, "Politik", "28.04"),

        # Storyline 8: "Die geheime Teeverkostung in der königlichen Familie"
        (219, "Geheime Teeverkostung im Buckingham Palace", 
        "Im Buckingham Palace fand kürzlich eine geheime Teeverkostung statt, bei der verschiedene Teesorten getestet wurden. Berichten zufolge könnte es sich um eine neue Initiative der königlichen Familie handeln, um das Land auf teegeschmackliche Innovationen vorzubereiten.", 
        True, None, None, 2, "Königsfamilie", "04.06"),

        (220, "Der königliche Teegarten als neues Projekt", 
        "Die königliche Familie plant, einen riesigen Teegarten im Buckingham Palace anzulegen, um ein einzigartiges Teeerlebnis zu schaffen. Experten berichten von einer königlichen Initiative, die den Teeimport aus Asien revolutionieren könnte.", 
        True, 219, 4, 2, "Wirtschaft", "07.06"),

        (221, "Königlicher Tee wird zum Trend", 
        "Die Teesorten aus dem Buckingham Palace erleben einen regelrechten Boom. Der königliche Tee aus dem Teegarten wird jetzt in den besten Londoner Salons serviert und erfreut sich einer immer größeren Anhängerschaft.", 
        True, 220, 5, 3, "Wirtschaft", "10.06"),

        # Storyline 9: "Die entlaufenen Tiere aus dem königlichen Zoo"
        (222, "Tierischer Ausbruch im königlichen Zoo", 
        "Mehrere Tiere aus dem königlichen Zoo in London sind aus ihren Gehegen entkommen. Die Polizei und der Zoo-Arbeiter versuchen verzweifelt, die Tiere einzufangen, bevor sie Schaden anrichten.", 
        True, None, None, 3, "Veranstaltung", "12.07"),

        (223, "Entlaufene Tiere fügen Chaos in der Stadt an", 
        "Die entlaufenen Tiere aus dem königlichen Zoo sind in die Straßen von London gelaufen und haben Chaos angerichtet. Berichten zufolge gab es mehrere Zwischenfälle, bei denen Passanten in Panik gerieten.", 
        True, 222, 4, 3, "Veranstaltung", "14.07"),

        (224, "Entlaufene Tiere wieder eingefangen", 
        "Die entlaufenen Tiere aus dem königlichen Zoo konnten schließlich eingefangen werden. Die Behörden untersuchen nun, wie es zu dem Ausbruch kam, und der Zoo hat angekündigt, Sicherheitsvorkehrungen zu verschärfen.", 
        True, 223, 5, 3, "Wirtschaft", "16.07"),

        # Storyline 10: "Das verborgene Manuskript der Alchemisten"
        (225, "Alchemistisches Manuskript aufgetaucht", 
        "Ein geheimnisvolles Manuskript, das angeblich von mittelalterlichen Alchemisten geschrieben wurde, ist auf einem Antiquitätenmarkt aufgetaucht. Historiker sind gespalten – einige glauben, es enthält geheimes Wissen, andere halten es für ein Fälschung.", 
        True, None, None, 3, "Wissenschaft", "01.08"),

        (226, "Manuskript entpuppt sich als echtes Artefakt", 
        "Das Manuskript von den mittelalterlichen Alchemisten wird nach eingehender Analyse als echtes Artefakt bestätigt. Historiker rätseln nun über die Bedeutung des Textes und welche Geheimnisse er bergen könnte.", 
        True, 225, 4, 3, "Wissenschaft", "03.08"),

        (227, "Das Geheimnis des Alchemistischen Manuskripts", 
        "Forscher versuchen nun, die Geheimnisse des alchemistischen Manuskripts zu entschlüsseln. Einige glauben, dass es Hinweise auf verloren geglaubtes Wissen enthält, das die Wissenschaft revolutionieren könnte.", 
        True, 226, 5, 3, "Wissenschaft", "06.08"),
        
        
        (1, "Kühner Bankraub erschüttert London", 
         "In den frühen Morgenstunden drangen unbekannte Täter in die Bank of England ein. Der Tresor wurde mit Sprengstoff geöffnet, "
         "wobei ein erheblicher Sachschaden entstand. Augenzeugen berichten von drei maskierten Gestalten, die sich in einer Pferdekutsche "
         "über die Fleet Street in Richtung Norden absetzten. Die Polizei hat eine Untersuchung eingeleitet und hofft auf Hinweise aus der Bevölkerung.",
         True, 2, 2, 3, "Einbruch", None),
        (2, "Das Geheimnis des Alchemistischen Manuskripts", 
         "Forscher versuchen nun, die Geheimnisse des alchemistischen Manuskripts zu entschlüsseln. Einige glauben, dass es Hinweise auf verloren geglaubtes Wissen enthält, das die Wissenschaft revolutionieren könnte.", 
         True, 226, 5, 3, "Wissenschaft", "06.08"),
        (3, "Erste dampfbetriebene Karussell in Bolton eröffnet", 
         "Revolutionäre Attraktion: Das erste dampfbetriebene Karussell begeistert die Besucher in Bolton! Mit Dampf betrieben, wird das Karussell ein neues Wahrzeichen der Stadt. Es wird erwartet, dass es die Attraktion von Bolton für die kommenden Jahre prägen wird. Die Technologie markiert einen bedeutenden Schritt in der Unterhaltungstechnik des 19. Jahrhunderts.", 
         True, None, None, 3, "Ankündigte Veranstaltung", "01.01"),
        (4, "Tod von Fanny Fleming, Schauspielerin (geb. 1796)", 
         "Großbritanniens Bühne verliert eine Legende: Schauspielerin Fanny Fleming im Alter von 29 Jahren verstorben. Fanny Fleming war bekannt für ihre beeindruckenden Auftritte in den Theatern Londons und galt als eine der besten Schauspielerinnen ihrer Zeit. Ihre tragische und frühe Abreise hinterlässt eine Lücke im kulturellen Leben der Nation.", 
         True, None, None, 3, "Tod", "17.01"),
        (5, "Tod von Catherine Gore, Schriftstellerin und Dramatikerin (geb. 1798)", 
         "Vermächtnis der Literatur: Catherine Gore, gefeierte Schriftstellerin, verstirbt im Alter von 63 Jahren. Catherine Gore war eine der einflussreichsten Schriftstellerinnen des 19. Jahrhunderts und prägte mit ihren Dramen die Theaterlandschaft.", 
         True, None, None, 3, "Tod", "29.01"),
        (6, "Tod von Bulkeley Bandinel, Bibliothekar (geb. 1781)", 
         "Abschied von einem Gelehrten: Bulkeley Bandinel, bedeutender Bibliothekar, stirbt im Alter von 80 Jahren. Bandinel war eine zentrale Figur der britischen Bibliothekswelt und ein Vorreiter in der Verwaltung und Katalogisierung von Sammlungen.", 
         True, None, None, 3, "Tod", "06.02"),
        (7, "Tod von John Brown, Geograph (geb. 1797)", 
         "Verlust für die Wissenschaft: Geograph John Brown, bekannt für seine Entdeckungen, verstorben. Brown hat das Verständnis der Geographie maßgeblich beeinflusst, indem er viele unbekannte Gebiete dokumentierte.", 
         True, None, None, 3, "Tod", "07.02"),
        (8, "Sträflinge übernehmen Gefängnis auf St. Mary's Island", 
         "Aufruhr im Chatham Dockyard: Etwa 350 Sträflinge übernehmen das Gefängnis auf St. Mary’s Island. In einer dramatischen Wendung gelang es den Häftlingen, das Gefängnis zu übernehmen und die Kontrolle zu übernehmen.", 
         True, None, None, 3, "Ereignis", "15.02"),
        (9, "Tod von Prinzessin Victoria von Sachsen-Coburg-Saalfeld, Herzogin von Kent", 
         "Ein königlicher Verlust: Prinzessin Victoria von Sachsen-Coburg-Saalfeld, Mutter von Königin Victoria, stirbt im Alter von 75 Jahren. Prinzessin Victoria war eine einflussreiche Figur am Hofe und eine tragende Säule der britischen Monarchie.", 
         True, None, None, 3, "Tod", "16.03"),
        (10, "Stürme beschädigen den Crystal Palace und die Kathedrale von Chichester", 
         "Unwetter zerstören Wahrzeichen: Crystal Palace beschädigt, Kirchturm von Chichester stürzt ein! Die verheerenden Stürme haben in London und Chichester enormen Schaden angerichtet.", 
         True, None, None, 3, "Wetterereignis", "20.02"),
        (11, "Großbrand in Tooley Street, Southwark", 
         "Feuer in Southwark: Brand zerstört mehrere Gebäude in der Tooley Street! Das verheerende Feuer brach in den frühen Morgenstunden aus und zerstörte zahlreiche Gebäude.", 
         True, None, None, 3, "Brand", "21.03"),
        (12, "William Crookes entdeckt Thallium", 
         "Wissenschaftlicher Durchbruch: William Crookes entdeckt das chemische Element Thallium! Diese Entdeckung öffnet neue Türen für die wissenschaftliche Forschung und könnte zukünftige Anwendungen in der Medizin und Technologie beeinflussen.", 
         True, None, None, 3, "Wissenschaft", "30.03"),
        (13, "Volkszählung im Vereinigten Königreich", 
         "Vereinigtes Königreich wächst: Volkszählung zeigt mehr als doppelt so viele Einwohner wie 1801, städtische Gebiete dominieren! Die Ergebnisse der Volkszählung zeigen einen dramatischen Anstieg der Bevölkerung.", 
         True, None, None, 3, "Wirtschaft", "07.04"),
        (14, "Tod von John Bartholomäus, Sr., Schottischer Kartograph (geb. 1805)", 
         "Die Welt der Kartographie verliert einen Pionier: John Bartholomäus, Schottischer Kartograph, verstorben. Bartholomäus war maßgeblich an der Schaffung von Karten beteiligt, die das britische Empire weltweit prägten.", 
         True, None, None, 3, "Tod", "08.04"),
        (15, "Beginn des amerikanischen Bürgerkriegs", 
         "Amerikanischer Bürgerkrieg entfacht – Auswirkungen auf Großbritannien und Lancashire Cotton Famine! Der amerikanische Bürgerkrieg hat nicht nur Auswirkungen auf die USA, sondern auch auf Großbritannien.", 
         True, None, None, 3, "Wirtschaft", "12.04"),
        (16, "Tod von Sir Hedworth Williamson, 7. Baronet, Politiker (geb. 1797)", 
         "Politisches Ende einer Ära: Sir Hedworth Williamson, 7. Baronet und Politiker, gestorben. Sir Hedworth Williamson war für seine politische Arbeit in verschiedenen Ämtern bekannt und hatte einen großen Einfluss auf die Politik der Zeit.", 
         True, None, None, 3, "Tod", "24.04"),
        (17, "Großbritannien erklärt Neutralität im amerikanischen Bürgerkrieg", 
         "Politische Entscheidung: Großbritannien bleibt im amerikanischen Bürgerkrieg neutral! Nach intensiven diplomatischen Beratungen gab die britische Regierung ihre Entscheidung bekannt, nicht in den amerikanischen Bürgerkrieg einzugreifen.", 
         True, None, None, 3, "Politik", "13.05"),
        (18, "Thomas Cook führt erste Pauschalreise nach Paris durch", 
         "Revolution des Reisens: Thomas Cook startet erste Pauschalreise von London nach Paris! Thomas Cook hat ein neues Kapitel in der Reisebranche aufgeschlagen, indem er die erste organisierte Pauschalreise nach Paris anbietet.", 
         True, None, None, 3, "Wirtschaft", "17.05"),
        (19, "Tod von Henry Gray, Anatom", 
         "Abschied von einem medizinischen Pionier: Anatom Henry Gray verstorben. Henry Gray war berühmt für seine Arbeiten über die menschliche Anatomie, die weltweit als Standardwerke gelten.", 
         True, None, None, 3, "Tod", "13.06"),
        (20, "Tod von Eaton Hodgkinson, Bauingenieur (geb. 1789)", 
         "Ein Verlust für die Ingenieurskunst: Eaton Hodgkinson, berühmter Bauingenieur, verstirbt. Hodgkinson war für seine wegweisenden Arbeiten im Bereich der Brücken- und Eisenkonstruktionen bekannt.", 
         True, None, None, 3, "Tod", "18.06"),
        (21, "Tod von Elizabeth Barrett Browning, Dichterin (geb. 1806)", 
         "Die literarische Welt trauert: Elizabeth Barrett Browning, bedeutende Dichterin, gestorben. Elizabeth Barrett Browning war eine der bekanntesten Dichterinnen der viktorianischen Ära.", 
         True, None, None, 3, "Tod", "29.06"),
        (22, "Gelbfieberausbruch auf HMS Firebrand", 
         "Tragödie auf See: 52 Tote durch Gelbfieberausbruch auf der HMS Firebrand in den Westindischen Inseln! Der Gelbfieberausbruch, der die Besatzung der HMS Firebrand heimsuchte, hat in den Westindischen Inseln eine verheerende Wirkung hinterlassen.", 
         True, None, None, 3, "Ereignis", "03.07"),
        
        # Vorherige Ereignisse bleiben bestehen...
        (16, "Tod von Sir Hedworth Williamson, 7. Baronet, Politiker (geb. 1797)", 
         "Politisches Ende einer Ära: Sir Hedworth Williamson, 7. Baronet und Politiker, gestorben. Sir Hedworth Williamson war für seine politische Arbeit in verschiedenen Ämtern bekannt und hatte einen großen Einfluss auf die Politik der Zeit.", 
         True, None, None, 3, "Tod", "24.04"),
        (17, "Großbritannien erklärt Neutralität im amerikanischen Bürgerkrieg", 
         "Politische Entscheidung: Großbritannien bleibt im amerikanischen Bürgerkrieg neutral! Nach intensiven diplomatischen Beratungen gab die britische Regierung ihre Entscheidung bekannt, nicht in den amerikanischen Bürgerkrieg einzugreifen.", 
         True, None, None, 3, "Politik", "13.05"),
        (18, "Thomas Cook führt erste Pauschalreise nach Paris durch", 
         "Revolution des Reisens: Thomas Cook startet erste Pauschalreise von London nach Paris! Thomas Cook hat ein neues Kapitel in der Reisebranche aufgeschlagen, indem er die erste organisierte Pauschalreise nach Paris anbietet.", 
         True, None, None, 3, "Wirtschaft", "17.05"),
        (19, "Tod von Henry Gray, Anatom", 
         "Abschied von einem medizinischen Pionier: Anatom Henry Gray verstorben. Henry Gray war berühmt für seine Arbeiten über die menschliche Anatomie, die weltweit als Standardwerke gelten.", 
         True, None, None, 3, "Tod", "13.06"),
        (20, "Tod von Eaton Hodgkinson, Bauingenieur (geb. 1789)", 
         "Ein Verlust für die Ingenieurskunst: Eaton Hodgkinson, berühmter Bauingenieur, verstirbt. Hodgkinson war für seine wegweisenden Arbeiten im Bereich der Brücken- und Eisenkonstruktionen bekannt.", 
         True, None, None, 3, "Tod", "18.06"),
        (21, "Tod von Elizabeth Barrett Browning, Dichterin (geb. 1806)", 
         "Die literarische Welt trauert: Elizabeth Barrett Browning, bedeutende Dichterin, gestorben. Elizabeth Barrett Browning war eine der bekanntesten Dichterinnen der viktorianischen Ära.", 
         True, None, None, 3, "Tod", "29.06"),
        (22, "Gelbfieberausbruch auf HMS Firebrand", 
         "Tragödie auf See: 52 Tote durch Gelbfieberausbruch auf der HMS Firebrand in den Westindischen Inseln! Der Gelbfieberausbruch, der die Besatzung der HMS Firebrand heimsuchte, hat in den Westindischen Inseln eine verheerende Wirkung hinterlassen.", 
         True, None, None, 3, "Ereignis", "03.07"),
        (23, "Tod von Sir Francis Palgrave, Historiker (geb. 1788)", 
         "Historische Verluste: Sir Francis Palgrave, Historiker und Autor, verstorben. Sir Francis Palgrave war bekannt für seine umfassenden Arbeiten zur englischen Geschichte, besonders im Bereich der mittelalterlichen und normannischen Studien.", 
         True, None, None, 3, "Tod", "06.07"),
        (24, "Tod von Richard Temple-Nugent-Brydges-Chandos-Grenville, 2. Duke of Buckingham and Chandos, Politiker (geb. 1797)", 
         "Adliger Abschied: Richard Temple-Nugent-Brydges-Chandos-Grenville, 2. Duke of Buckingham, verstorben. Der 2. Duke of Buckingham war für seine politischen und philanthropischen Bemühungen bekannt.", 
         True, None, None, 3, "Tod", "29.07"),
        (25, "Konkurs- und Insolvenzgesetz kodifiziert Gesellschaftsrecht", 
         "Neues Gesetz: Konkurs- und Insolvenzgesetz reformiert Gesellschaftsrecht im Vereinigten Königreich! Das neue Gesetz bringt umfassende Änderungen für Unternehmen und deren Gläubiger und stellt sicher, dass Insolvenzen fairer und geordneter abgewickelt werden.", 
         True, None, None, 3, "Politik", "31.07"),
        (26, "Strafrechtskonsolidierungsgesetze erlangen königliche Zustimmung", 
         "Die Konsolidierung der britischen Strafgesetze bringt mehr Klarheit und Einheitlichkeit in die Rechtsprechung des Landes. Diese Reform wird als Schritt hin zu einem gerechteren und transparenteren Rechtssystem angesehen.", 
         True, None, None, 3, "Politik", "06.08"),
        (27, "Letzte Hinrichtung wegen versuchten Mordes in Großbritannien", 
         "Mit der Hinrichtung eines Mannes, der des versuchten Mordes beschuldigt wurde, wird ein historisches Kapitel im britischen Strafrecht abgeschlossen. Diese Entscheidung zeigt den Übergang hin zu weniger brutalen Strafen und einem humaneren Strafrechtssystem.", 
         True, None, None, 3, "Recht", "27.08"),
        (28, "Tod von Ernest Edgcumbe, 3. Earl of Mount Edgcumbe, Politiker (geb. 1797)", 
         "Ernest Edgcumbe war für seine bedeutende Rolle in der britischen Politik und seine Mitgliedschaft im House of Lords bekannt. Er setzte sich für soziale Reformen ein und wurde als einer der einflussreichsten Aristokraten seiner Zeit geschätzt.", 
         True, None, None, 3, "Tod", "03.09"),
        (29, "Eröffnung der Postsparbank", 
         "Mit der Eröffnung der ersten Postsparbank wird ein neues Kapitel im britischen Bankwesen aufgeschlagen, das Millionen von Menschen den Zugang zu sicheren Sparmöglichkeiten bietet.", 
         True, None, None, 3, "Wirtschaft", "16.09"),
        (30, "Tod von Archibald Montgomerie, 13. Earl of Eglinton, Edelmann (geb. 1812)", 
         "Der 13. Earl of Eglinton war ein respektierter Adliger, der nicht nur in politischen Kreisen eine Rolle spielte, sondern auch in der Schottischen Gesellschaft großen Einfluss hatte.", 
         True, None, None, 3, "Tod", "04.10"),
        (31, "Tod von William Ranwell, Meeresmaler (geb. 1797)", 
         "William Ranwell galt als ein herausragender Maler der maritimen Kunst und seine Werke fangen das raue Leben auf See mit außergewöhnlicher Präzision und Detailtreue ein.", 
         True, None, None, 3, "Tod", "05.10"),
        (32, "Tod von Sir William Cubitt, Bauingenieur (geb. 1785)", 
         "Sir William Cubitt war berühmt für seine Arbeiten im Bereich der Infrastruktur, insbesondere beim Bau von Eisenbahnen und Brücken. Viele seiner Ingenieursprojekte, die über Großbritannien verstreut sind, bleiben bis heute von entscheidender Bedeutung für das nationale Verkehrsnetz.", 
         True, None, None, 3, "Tod", "13.10"),
        
        # Vorherige Ereignisse bleiben bestehen...
        (33, "Tod von Edward Dickinson Baker, US-Senator aus Oregon (geb. 1811 in Großbritannien)", 
         "Edward Dickinson Baker war der einzige US-Senator, der im amerikanischen Bürgerkrieg kämpfte und dabei sein Leben verlor. Er hatte sich im Senat für die Rechte der Union eingesetzt und war eine prominente Figur der politischen Landschaft.", 
         True, None, None, 3, "Tod", "21.10"),
        (34, "Fertigstellung der HMS Warrior", 
         "Die HMS Warrior ist ein technisches Meisterwerk der Ingenieurskunst und setzt neue Maßstäbe für die Kriegsschifffahrt. Mit ihrer eisernen Hülle und modernster Waffentechnologie wird sie als das fortschrittlichste Kriegsschiff ihrer Zeit angesehen.", 
         True, None, None, 3, "Technologie", "24.10"),
        (35, "Trent Affair: USA greifen britisches Postschiff an", 
         "Die Trent Affair löst eine diplomatische Krise zwischen Großbritannien und den USA aus, nachdem ein britisches Postschiff von einem amerikanischen Kriegsschiff angegriffen wurde. Dies führt zu internationalen Spannungen und ernsthaften Verhandlungen.", 
         True, None, None, 3, "Politik", "08.11"),
        (36, "Tod von Arthur Hugh Clough, Dichter (geb. 1819)", 
         "Arthur Hugh Clough war bekannt für seine intellektuellen Gedichte und seine kritische Haltung gegenüber gesellschaftlichen Normen. Als Vertreter des viktorianischen Zweifels und einer neuen literarischen Bewegung war er eine Schlüsselfigur in der englischen Dichtung.", 
         True, None, None, 3, "Tod", "13.11"),
        (37, "Tod von Sir John Forbes, königlicher Arzt (geb. 1787)", 
         "Sir John Forbes war ein Pionier der modernen Medizin und trug wesentlich zur medizinischen Ausbildung in Großbritannien bei. Er war bekannt für seine Arbeiten in der öffentlichen Gesundheit und seine Bemühungen um die Verbesserung der medizinischen Versorgung für alle.", 
         True, None, None, 3, "Tod", "13.11"),
        (38, "Tod von John Hodgetts-Foley, Politiker (geb. 1797)", 
         "John Hodgetts-Foley war eine einflussreiche politische Figur und spielte eine zentrale Rolle in der Entwicklung der britischen Gesetzgebung. Mit seiner klugen Politikgestaltung und seinem Engagement für die soziale Gerechtigkeit war er ein respektierter Mann.", 
         True, None, None, 3, "Tod", "13.11"),
        (39, "Einsturz eines Mietshauses in Edinburgh", 
         "Der Einsturz eines historischen Mietshauses hat die schottische Hauptstadt erschüttert und eine Welle der Bestürzung ausgelöst. Die Tragödie wirft ein Schlaglicht auf die Sicherheitsstandards im städtischen Wohnungsbau der Zeit.", 
         True, None, None, 3, "Ereignis", "25.11"),
        (40, "Großbritannien reagiert auf Trent Affair", 
         "Politische Spannung: Großbritannien sendet Antwort auf die Trent Affair und zeigt diplomatische Entschlossenheit! Die britische Regierung hat eine entschlossene Antwort auf die amerikanische Aggression gezeigt, indem sie diplomatische Maßnahmen ergriffen hat.", 
         True, None, None, 3, "Politik", "01.12"),
        (41, "Tod von Thomas Southwood Smith, Arzt und Sanitär-Reformer (geb. 1788)", 
         "Thomas Southwood Smith war ein führender Verfechter der öffentlichen Gesundheit und hat maßgeblich zur Verbesserung der sanitären Bedingungen in Großbritannien beigetragen. Durch seine Studien und Empfehlungen hat er das Verständnis für den Zusammenhang zwischen Hygiene und Gesundheit revolutioniert.", 
         True, None, None, 3, "Tod", "10.12"),
        (42, "Tod von Albert, Prinz Consort, Ehegatte von Königin Victoria (geb. 1819 in Deutschland)", 
         "Der Tod von Prinz Albert hinterlässt eine unermessliche Lücke am britischen Hof. Als Berater und Partner von Königin Victoria war er eine entscheidende Figur in der politischen und sozialen Entwicklung des Vereinigten Königreichs.", 
         True, None, None, 3, "Tod", "14.12"),
        (43, "James Clerk Maxwell enthüllt bahnbrechende Dreifarbenfotografie", 
         "In einem spektakulären Experiment, das das Potenzial der Fotografie für immer verändern wird, präsentierte James Clerk Maxwell heute der Welt seine bahnbrechende Dreifarbenfotografie. Der schottische Physiker kombinierte die Grundfarben Rot, Grün und Blau, um ein lebendiges, farbiges Bild zu erzeugen.", 
         True, None, None, 3, "Technologie", "24.02"),
        (44, "Großbritannien richtet strategische Stützpunkte in Lagos ein, um den Sklavenhandel zu zerschlagen", 
         "Mit einer dramatischen Wende im Kampf gegen das unmenschliche Geschäft des Sklavenhandels errichtet das britische Empire nun strategische Stützpunkte in Lagos, Nigeria, um dem blutigen Handel endgültig ein Ende zu setzen.", 
         True, None, None, 3, "Politik", "03.03"),
        (45, "Historischer Friedensvertrag zwischen Bahrain und Großbritannien unterzeichnet", 
         "In einem sensationellen diplomatischen Durchbruch haben Bahrain und Großbritannien den „Perpetual Truce of Peace and Friendship“-Vertrag unterzeichnet – ein Abkommen, das die Grundlage für eine neue Ära der Zusammenarbeit in der strategischen Region des Nahen Ostens legt.", 
         True, None, None, 3, "Politik", "12.05"),
        (46, "Einweihung der ältesten griechisch-orthodoxen Kirche Englands in Manchester", 
         "Ein stolzer Moment für die griechische Gemeinde in Großbritannien, als die griechisch-orthodoxe Kirche der Verkündigung in Manchester feierlich eingeweiht wurde – die älteste ihrer Art in England!", 
         True, None, None, 3, "Ereignis", "15.06"),
        (47, "Baubeginn des Royal Museums in Edinburgh – ein Meisterwerk für die Ewigkeit!", 
         "Ein historischer Tag für Schottland: Der Bau des Royal Museums in Edinburgh hat begonnen! Das monumentale Projekt verspricht, eines der größten kulturellen Wahrzeichen des Empire zu werden und eine unschätzbare Sammlung von Kunstwerken und wissenschaftlichen Schätzen zu beherbergen.", 
         True, None, None, 3, "Kultur", "28.06"),
        (48, "Krimkriegsdenkmal in London enthüllt – Britische Helden geehrt!", 
         "Ein atemberaubendes Denkmal zur Ehrung der britischen Kriegshelden wurde heute in London enthüllt. Die prachtvollen Skulpturen von „Other Ranks“ würdigen die tapferen Soldaten, die im Krimkrieg für das Empire ihr Leben gaben.", 
         True, None, None, 3, "Ereignis", "18.07"),
        (49, "William Morris revolutioniert das Möbeldesign mit Morris, Marshall, Faulkner & Co.", 
         "Ein neuer Stern am Firmament der Designwelt: William Morris hat heute das Möbelunternehmen „Morris, Marshall, Faulkner & Co.“ gegründet – ein Unternehmen, das Kunst und Handwerkskunst auf das höchste Podium stellt!", 
         True, None, None, 3, "Unternehmen", "03.09"),
        (50, "Einladung zur Gründonnerstagsmesse", 
         "Am Gründonnerstag, den 28. März, lädt die St. Marys Church alle Gläubigen zu einer besinnlichen Messe ein, um das letzte Abendmahl unseres Herrn Jesus Christus zu gedenken. Der Gottesdienst beginnt um 18 Uhr und wird von Pfarrer O’Sullivan zelebriert. Treten Sie ein in die Stille und Besinnung des Gründonnerstags, in dem wir uns auf das Leiden und die Auferstehung unseres Erlösers vorbereiten.", 
         True, None, None, 3, "Kirche", "26.03"),
        (51, "Einladung zur Ostermontagsmesse – 28. März 1861", 
         "Am Ostermontag, den 1. April, lädt die St. Marys Church zu einer besonderen Messe ein, die den Weg der Jünger von Emmaus in den Mittelpunkt stellt. Die Messe beginnt um 10 Uhr, und Pfarrer O’Sullivan wird die tiefere Bedeutung dieses biblischen Ereignisses erläutern.", 
         True, None, None, 3, "Kirche", "28.03"),
        (52, "Einladung zur Feier des Ersten Weihnachtsfeiertages – 25. Dezember 1861", 
         "Am 25. Dezember, dem ersten Weihnachtsfeiertag, laden wir Sie herzlich ein, mit uns die Geburt unseres Erlösers zu feiern. Der Gottesdienst beginnt um 10 Uhr und wird von Pfarrer O’Sullivan gehalten. In seiner Predigt wird er die Freude und das Wunder der Geburt Christi hervorheben.", 
         True, None, None, 3, "Kirche", "25.12"),
        (53, "Einladung zur Feier des Zweiten Weihnachtsfeiertages – 26. Dezember 1861", 
         "Am 26. Dezember, dem zweiten Weihnachtsfeiertag, laden wir Sie ein, weiterhin das große Geheimnis der Geburt Christi zu feiern. Der Gottesdienst beginnt um 10 Uhr, und auch an diesem Tag wird Pfarrer O’Sullivan die Bedeutung dieses heiligen Festes für uns alle verdeutlichen.", 
         True, None, None, 3, "Kirche", "26.12"),
        (54, "Aschermittwoch in der St. Marys Church: Beginn der Fastenzeit", 
         "Die St. Marys Church lädt alle Gläubigen am kommenden Mittwoch, den 13. Februar, zur feierlichen Aschermittwochsmesse ein. Der Beginn der Fastenzeit ist ein Moment der Besinnung und Buße, und Pfarrer O’Sullivan wird in seiner Predigt die Bedeutung der inneren Reinigung und der Umkehr betonen.", 
         True, None, None, 3, "Kirche", "11.02"),
        (55, "Karfreitag in der St. Marys Church: Gedenken des Leidens Christi", 
         "Am Freitag, den 29. März, lädt die St. Marys Church zur feierlichen Karfreitagsmesse ein, um das Leiden und Sterben Christi zu gedenken. Pfarrer O’Sullivan wird die Passion Christi in einer bewegenden Predigt erörtern.", 
         True, None, None, 3, "Kirche", "27.03"),
        (56, "Ostersonntag in der St. Marys Church: Die Auferstehung Christi feiern", 
         "Am Sonntag, den 31. März, wird die St. Marys Church zum Ort der Feierlichkeit und Freude, wenn wir die Auferstehung unseres Herrn Jesus Christus feiern. Der Ostergottesdienst beginnt um 10 Uhr, und Pfarrer O’Sullivan wird die frohe Botschaft der Auferstehung verkünden.", 
         True, None, None, 3, "Kirche", "29.03"),
        (50, "Einladung zur Gründonnerstagsmesse", 
         "Am Gründonnerstag, den 28. März, lädt die St. Marys Church alle Gläubigen zu einer besinnlichen Messe ein, um das letzte Abendmahl unseres Herrn Jesus Christus zu gedenken. Der Gottesdienst beginnt um 18 Uhr und wird von Pfarrer O’Sullivan zelebriert. Treten Sie ein in die Stille und Besinnung des Gründonnerstags, in dem wir uns auf das Leiden und die Auferstehung unseres Erlösers vorbereiten.", 
         True, None, None, 3, "Kirche", "26.03"),
        (51, "Einladung zur Ostermontagsmesse – 28. März 1861", 
         "Am Ostermontag, den 1. April, lädt die St. Marys Church zu einer besonderen Messe ein, die den Weg der Jünger von Emmaus in den Mittelpunkt stellt. Die Messe beginnt um 10 Uhr, und Pfarrer O’Sullivan wird die tiefere Bedeutung dieses biblischen Ereignisses erläutern.", 
         True, None, None, 3, "Kirche", "28.03"),
        (52, "Einladung zur Feier des Ersten Weihnachtsfeiertages – 25. Dezember 1861", 
         "Am 25. Dezember, dem ersten Weihnachtsfeiertag, laden wir Sie herzlich ein, mit uns die Geburt unseres Erlösers zu feiern. Der Gottesdienst beginnt um 10 Uhr und wird von Pfarrer O’Sullivan gehalten. In seiner Predigt wird er die Freude und das Wunder der Geburt Christi hervorheben.", 
         True, None, None, 3, "Kirche", "25.12"),
        (53, "Einladung zur Feier des Zweiten Weihnachtsfeiertages – 26. Dezember 1861", 
         "Am 26. Dezember, dem zweiten Weihnachtsfeiertag, laden wir Sie ein, weiterhin das große Geheimnis der Geburt Christi zu feiern. Der Gottesdienst beginnt um 10 Uhr, und auch an diesem Tag wird Pfarrer O’Sullivan die Bedeutung dieses heiligen Festes für uns alle verdeutlichen.", 
         True, None, None, 3, "Kirche", "26.12"),
        (54, "Aschermittwoch in der St. Marys Church: Beginn der Fastenzeit", 
         "Die St. Marys Church lädt alle Gläubigen am kommenden Mittwoch, den 13. Februar, zur feierlichen Aschermittwochsmesse ein. Der Beginn der Fastenzeit ist ein Moment der Besinnung und Buße, und Pfarrer O’Sullivan wird in seiner Predigt die Bedeutung der inneren Reinigung und der Umkehr betonen.", 
         True, None, None, 3, "Kirche", "11.02"),
        (55, "Karfreitag in der St. Marys Church: Gedenken des Leidens Christi", 
         "Am Freitag, den 29. März, lädt die St. Marys Church zur feierlichen Karfreitagsmesse ein, um das Leiden und Sterben Christi zu gedenken. Pfarrer O’Sullivan wird die Passion Christi in einer bewegenden Predigt erörtern.", 
         True, None, None, 3, "Kirche", "27.03"),
        (56, "Ostersonntag in der St. Marys Church: Die Auferstehung Christi feiern", 
         "Am Sonntag, den 31. März, wird die St. Marys Church zum Ort der Feierlichkeit und Freude, wenn wir die Auferstehung unseres Herrn Jesus Christus feiern. Der Ostergottesdienst beginnt um 10 Uhr, und Pfarrer O’Sullivan wird die frohe Botschaft der Auferstehung verkünden.", 
         True, None, None, 3, "Kirche", "29.03"),
        (57, "Christi Himmelfahrt in der St. Marys Church: Feier des Himmelfahrtsfestes", 
         "Am kommenden Donnerstag, den 9. Mai, wird die St. Marys Church die Feier der Christi Himmelfahrt mit einer feierlichen Messe begehen. Der Gottesdienst beginnt um 10 Uhr, und Pfarrer O’Sullivan wird die Bedeutung des Himmelfahrtsfestes erklären, das den triumphalen Aufstieg Jesu in den Himmel nach seiner Auferstehung gedenkt.", 
         True, None, None, 3, "Kirche", "07.05"),
        (58, "Pfingstsonntag in der St. Marys Church: Der Heilige Geist kommt", 
         "Am Sonntag, den 19. Mai, wird die St. Marys Church den Pfingstsonntag mit einer besonderen Messe feiern, um die Herabkunft des Heiligen Geistes zu ehren. Die Messe beginnt um 11 Uhr, und Pfarrer O’Sullivan wird die Bedeutung des Pfingstfestes erklären.", 
         True, None, None, 3, "Kirche", "17.05"),
        (59, "Pfingstmontag in der St. Marys Church: Weiterfeier des Pfingstfestes", 
         "Am Montag, den 20. Mai, wird die St. Marys Church ihre Feierlichkeiten zum Pfingstfest fortsetzen. Die Messe beginnt um 10 Uhr, und Pfarrer O’Sullivan wird sich auf die Einheit der Christen durch den Heiligen Geist konzentrieren.", 
         True, None, None, 3, "Kirche", "19.05"),
        (60, "Fronleichnam in der St. Marys Church: Feier der Eucharistie", 
         "Am Donnerstag, den 30. Mai, lädt die St. Marys Church zur Feier des Fronleichnamsfestes ein, bei dem wir die heilige Eucharistie und das wahre Brot des Lebens verehren. Die Prozession beginnt um 18 Uhr, gefolgt von einer feierlichen Messe.", 
         True, None, None, 3, "Kirche", "28.05"),
        (61, "Buß- und Bettag in der St. Marys Church: Ein Tag der Umkehr", 
         "Am Mittwoch, den 20. November, wird die St. Marys Church den Buß- und Bettag mit einer bewegenden Messe begehen. Der Gottesdienst beginnt um 19 Uhr, und Pfarrer O’Sullivan wird die Bedeutung der Buße und der Umkehr für das christliche Leben betonen.", 
         True, None, None, 3, "Kirche", "18.11"),
        (62, "Totensonntag in der St. Marys Church: Gedenken der Verstorbenen", 
         "Am Sonntag, den 24. November, wird die St. Marys Church zum Ort der Erinnerung und des Gebets, wenn wir der Verstorbenen gedenken. Die Messe beginnt um 10 Uhr, und Pfarrer O’Sullivan wird mit einer besonderen Predigt die Bedeutung des Totensonntags für unsere christliche Hoffnung und das ewige Leben vertiefen.", 
         True, None, None, 3, "Kirche", "22.11"),
        (63, "Erster Advent in der St. Marys Church: Beginn der Adventszeit", 
         "Am Sonntag, den 1. Dezember, beginnt in der St. Marys Church die festliche Adventszeit mit einer feierlichen Messe. Der Gottesdienst beginnt um 10 Uhr, und Pfarrer O’Sullivan wird die Bedeutung der Adventszeit erläutern.", 
         True, None, None, 3, "Kirche", "29.11"),
        (64, "Zweiter Advent in der St. Marys Church: Der Weg des Lichtes", 
         "Am Sonntag, den 8. Dezember, lädt die St. Marys Church zum zweiten Adventsgottesdienst ein. Die Messe beginnt um 10 Uhr, und Pfarrer O’Sullivan wird die Bedeutung des Lichts Christi in einer dunklen Welt verkünden.", 
         True, None, None, 3, "Kirche", "06.12"),
        (65, "Dritter Advent in der St. Marys Church: Freude in der Erwartung", 
         "Am Sonntag, den 15. Dezember, wird in der St. Marys Church der dritte Advent gefeiert. Der Gottesdienst beginnt um 10 Uhr, und Pfarrer O’Sullivan wird die Freude und Hoffnung verkünden, die die Adventszeit mit sich bringt.", 
         True, None, None, 3, "Kirche", "13.12"),
        (66, "Vierter Advent in der St. Marys Church: Der Weg zum Heiligtum", 
         "Am Sonntag, den 22. Dezember, lädt die St. Marys Church zum letzten Adventsgottesdienst vor Weihnachten ein. Der Gottesdienst beginnt um 10 Uhr, und Pfarrer O’Sullivan wird uns auf den Höhepunkt der Adventszeit vorbereiten.", 
         True, None, None, 3, "Kirche", "20.12"),
        (67, "Heiligabend in der St. Marys Church: Die Nacht der Geburt Christi", 
         "Am Abend des 24. Dezember lädt die St. Marys Church zu einer festlichen Heiligabendmesse ein. Der Gottesdienst beginnt um 23 Uhr, und Pfarrer O’Sullivan wird die Frohe Botschaft der Geburt Christi verkünden.", 
         True, None, None, 3, "Kirche", "22.12"),
        (1, "Eröffnung der neuen Kunstgalerie im British Museum", 
        "Heute wurde eine neue Galerie im British Museum eröffnet, die eine beeindruckende Sammlung von Renaissance-Meisterwerken zeigt. Die Ausstellung umfasst Werke von berühmten Künstlern wie Leonardo da Vinci und Michelangelo. Kunstliebhaber aus der ganzen Stadt strömten herbei, um diese außergewöhnliche Sammlung zu bewundern.", 
        True, 4, 3, 3, "Kunst", "21.04"),
        
        (2, "Moderne Malerei im Victoria and Albert Museum", 
        "Das Victoria and Albert Museum hat eine neue Ausstellung zur modernen Malerei des 19. Jahrhunderts eröffnet. Werke von britischen Künstlern wie J.M.W. Turner und John Constable sind nun zu sehen. Besucher können die Entwicklung der Kunst in Großbritannien und die Veränderungen in der Darstellung der Landschaft erleben.", 
        True, 5, 4, 2, "Kunst", "21.05"),
        
        (3, "Prähistorische Kunst im British Museum enthüllt", 
        "Eine neue Ausstellung im British Museum widmet sich der prähistorischen Kunst. Skulpturen und Höhlenmalereien aus der Altsteinzeit wurden erstmals der Öffentlichkeit zugänglich gemacht. Diese Entdeckungen bieten einen einzigartigen Blick auf die frühen künstlerischen Ausdrucksformen der Menschheit.", 
        True, 4, 2, 4, "Kunst", "21.06"),
        
        (4, "Antike Meisterwerke im National Gallery eröffnet", 
        "Die National Gallery hat eine bedeutende Sammlung antiker Kunstwerke aus Griechenland und Rom ausgestellt. Statuen, Töpferwaren und Wandmalereien zeigen das künstlerische Erbe der antiken Zivilisationen. Die Ausstellung ist eine Hommage an die Kunstfertigkeit dieser vergangenen Kulturen.", 
        True, 6, 3, 3, "Kunst", "21.04"),
        
        (5, "Erste Retrospektive von Thomas Gainsborough im Tate Gallery", 
        "Die Tate Gallery feiert mit einer retrospektiven Ausstellung das Werk des berühmten Malers Thomas Gainsborough. Die Sammlung umfasst einige seiner bekanntesten Porträts und Landschaften. Diese Präsentation wird von Kunstkritikern als ein Meilenstein in der Feier der britischen Malerei des 18. Jahrhunderts betrachtet.", 
        True, 7, 5, 2, "Kunst", "25.05"),
        
        (6, "Die Welt der viktorianischen Mode im Victoria and Albert Museum", 
        "Eine neue Ausstellung im Victoria and Albert Museum beleuchtet die Entwicklung der viktorianischen Mode. Vom prächtigen Ballkleid bis hin zu alltäglichen Kleidungsstücken wird die Vielfalt der Mode im 19. Jahrhundert gezeigt. Die Ausstellung bietet einen faszinierenden Einblick in die gesellschaftlichen Normen und Veränderungen jener Zeit.", 
        True, 5, 4, 4, "Mode", "30.03"),
        
        (7, "Neue Ausstellung zu englischer Porzellan-Kunst im British Museum", 
        "Das British Museum hat eine faszinierende Ausstellung über englische Porzellan-Kunst eröffnet. Die Sammlungen umfassen Werke von renommierten Manufakturen wie Wedgwood und Royal Worcester. Besucher können die Feinheit und Eleganz des englischen Porzellans bewundern.", 
        True, 4, 3, 3, "Kunst", "02.03"),
        
        (8, "Die Ägyptische Sammlung im British Museum erweitert", 
        "Das British Museum hat seine Ausstellung zur ägyptischen Kunst und Kultur mit neuen Funden erweitert. Die Besucher können nun eine Reihe von antiken Skulpturen, Hieroglyphen und Mumien aus dem alten Ägypten bewundern. Diese Erweiterung hat die Sammlung des Museums auf ein neues Niveau gehoben.", 
        True, 6, 3, 3, "Kunst", "22.03"),
        
        (9, "Das Werk von Sir George Beaumont im Tate Gallery", 
        "Die Tate Gallery hat eine umfassende Ausstellung zu den Arbeiten des Malers Sir George Beaumont eröffnet. Neben seinen bekannten Landschaftsgemälden werden auch zahlreiche seiner Skizzen und Studien gezeigt. Diese Ausstellung bietet einen einzigartigen Einblick in das kreative Schaffen eines der führenden Künstler der englischen Romantik.", 
        True, 7, 5, 2, "Kunst", "23.03"),
        
        (10, "Neue Sammlung von asiatischer Kunst im Victoria and Albert Museum", 
        "Das Victoria and Albert Museum hat eine neue Sammlung von asiatischer Kunst eröffnet, die Werke aus China, Japan und Indien umfasst. Die Ausstellung zeigt meisterhafte Kunstwerke wie Teppiche, Töpferwaren und Schmuck aus dem Fernen Osten. Diese Präsentation unterstreicht die weltweite Bedeutung asiatischer Kunst im 19. Jahrhundert.", 
        True, 5, 4, 2, "Kunst", "25.03"),
        
        (11, "Hochmittelalterliche Kunst im British Museum", 
        "Eine neue Ausstellung im British Museum widmet sich der hochmittelalterlichen Kunst. Die Sammlung umfasst leuchtend bunte Manuskripte, Skulpturen und liturgische Kunstwerke aus dem 12. bis 14. Jahrhundert. Besucher können einen faszinierenden Blick auf die religiöse und kulturelle Welt des Mittelalters werfen.", 
        True, 4, 2, 4, "Kunst", "09.03"),
        
        (12, "Indische Miniaturmalerei im Victoria and Albert Museum", 
        "Im Victoria and Albert Museum ist eine neue Ausstellung über die kunstvolle indische Miniaturmalerei eröffnet worden. Gezeigt werden Werke aus verschiedenen Regionen Indiens, die Szenen aus dem Alltag und der Mythologie darstellen. Diese zarten und detaillierten Werke bieten einen Einblick in die reiche Tradition indischer Kunst.", 
        True, 5, 4, 2, "Kunst", "19.04"),
        
        (13, "Neue Ausstellung zur englischen Architektur im British Museum", 
        "Eine neue Ausstellung im British Museum beleuchtet die Entwicklung der englischen Architektur vom Mittelalter bis in die viktorianische Ära. Modelle von berühmten Gebäuden, Pläne und Zeichnungen bieten einen faszinierenden Blick auf die Meisterwerke der englischen Architekturgeschichte. Die Ausstellung wird von Architekten und Historikern gleichermaßen geschätzt.", 
        True, 4, 3, 3, "Architektur", "06.07"),
        
        (14, "Die Kunst der viktorianischen Karikatur im Tate Gallery", 
        "Im Tate Gallery wird die Kunst der viktorianischen Karikatur mit einer neuen Ausstellung gewürdigt. Gezeigt werden Werke von berühmten Karikaturisten wie George Cruikshank und James Whistler. Diese humorvollen und oft gesellschaftskritischen Arbeiten spiegeln die politischen und sozialen Spannungen des 19. Jahrhunderts wider.", 
        True, 7, 5, 4, "Karikatur", "03.03"),

        (1, "Ein Blick auf die Kunst der Romantik im Victoria and Albert Museum", 
        "Das Victoria and Albert Museum hat eine bemerkenswerte Ausstellung zur Kunst der Romantik eröffnet. Mit Werken von Künstlern wie John Constable und Francisco Goya wird die emotionale und naturverbundene Strömung dieser Epoche lebendig. Die Ausstellung vermittelt eindrucksvoll die weltanschaulichen und ästhetischen Grundsätze der Romantik.", 
        True, 4, 3, 3, "Kunst", None),
        
        (2, "Neue Sammlung von Kunstwerken aus den Kolonien im British Museum", 
        "Das British Museum hat eine Sammlung von Kunstwerken aus den britischen Kolonien eröffnet, die beeindruckende Objekte aus Indien, Afrika und der Karibik umfasst. Diese Ausstellung beleuchtet die kulturellen Einflüsse der Kolonien auf die Kunstproduktion und zeigt, wie diese Kunstwerke die britische Wahrnehmung anderer Kulturen prägten.", 
        True, 6, 4, 2, "Kunst", None),
        
        (3, "Die Kunst des Rokoko im Victoria and Albert Museum", 
        "Eine neue Ausstellung im Victoria and Albert Museum widmet sich der Kunst des Rokoko, einer Periode der französischen Kunst, die sich durch verspielte und raffinierte Stile auszeichnet. Die Ausstellung umfasst Möbel, Malerei und Schmuckstücke dieser prunkvollen Ära. Besucher können die opulente Ästhetik des 18. Jahrhunderts erleben.", 
        True, 5, 3, 4, "Kunst", None),
        
        (4, "Neue Ausstellung zur viktorianischen Fotografie im British Museum", 
        "Das British Museum zeigt eine neue Ausstellung zur viktorianischen Fotografie, die die Entwicklung dieses neuen Mediums im 19. Jahrhundert beleuchtet. Fotografien von berühmten Porträtfotografen wie Julia Margaret Cameron und Roger Fenton bieten einen einzigartigen Einblick in das viktorianische England. Die Ausstellung zeigt auch, wie Fotografie als Kunstform anerkannt wurde.", 
        True, 7, 5, 3, "Fotografie", None),
        
        (5, "Sammlung von Kunstwerken der Präraffaeliten im Tate Gallery", 
        "Die Tate Gallery hat eine umfassende Sammlung von Kunstwerken der Präraffaeliten eröffnet. Werke von Dante Gabriel Rossetti, John Everett Millais und William Holman Hunt sind nun zu sehen. Die Ausstellung bietet einen tiefen Einblick in diese kunsthistorische Bewegung, die sich gegen die Industrialisierung und für eine Rückkehr zu einer idealisierten Natur wandte.", 
        True, 6, 4, 2, "Kunst", None),
        
        (6, "Die Entwicklung der Theaterkostüme im Victoria and Albert Museum", 
        "Im Victoria and Albert Museum wird eine neue Ausstellung über die Entwicklung der Theaterkostüme eröffnet. Die Sammlung zeigt prächtige Bühnenoutfits aus den letzten hundert Jahren, die von den größten britischen Theaterhäusern getragen wurden. Die Ausstellung unterstreicht die Bedeutung von Kostümdesign als Teil der kulturellen Darbietung auf der Bühne.", 
        True, 5, 3, 4, "Mode", None),
        
        (7, "Die Neue Eisenbahnverbindung zwischen London und Birmingham eröffnet!", 
        "Die neue Bahnstrecke, die London mit Birmingham verbindet, wurde gestern feierlich eingeweiht. Die Strecke, die in nur drei Stunden befahren werden kann, verspricht eine Revolution im Reiseverkehr und wird den Handel zwischen den beiden Städten erheblich ankurbeln. Experten begrüßen das Projekt als einen bedeutenden Fortschritt in der britischen Infrastruktur.", 
        True, 8, 6, 2, "Infrastruktur", None),
        
        (8, "Einführung des neuen Gaslichts in den Londoner Straßen", 
        "Ab morgen wird in vielen Teilen Londons das neue Gaslicht die nächtlichen Straßen erleuchten, was zu einer sichereren und effizienteren Beleuchtung führt. Dieses innovative System wurde von der 'London Gas Light Company' entwickelt und stellt einen großen Fortschritt im Vergleich zu den bisherigen Kerzenbeleuchtungen dar. Die Stadtverwaltung erhofft sich von dieser Veränderung eine Verbesserung der öffentlichen Sicherheit und des nächtlichen Verkehrs.", 
        True, 4, 3, 3, "Technologie", None),
        
        (9, "Queen Victoria besucht das Great Exhibition in Crystal Palace", 
        "Königin Victoria hat heute den Crystal Palace besucht, um die Weltausstellung zu eröffnen, die bahnbrechende Technologien aus der ganzen Welt präsentiert. Die Ausstellung zeigt unter anderem die neuesten Entwicklungen in der Maschinenindustrie, der Kunstfertigkeit und den wissenschaftlichen Entdeckungen. Der Besuch von Her Majesty wurde von Tausenden von Londonern begeistert verfolgt und wird als Meilenstein in der Geschichte der Expositionen gefeiert.", 
        True, 7, 5, 2, "Weltausstellung", None),
        
        (10, "Kampf gegen Cholera: Neue Hygienemaßnahmen in London eingeführt", 
        "Inmitten der Choleraepidemie, die London in den letzten Monaten erschüttert hat, haben die Behörden neue Hygienevorschriften eingeführt. Ab sofort werden alle öffentlichen Wasserquellen strengen Qualitätskontrollen unterzogen, und Abwasserkanäle sollen strikt überwacht werden, um die Ausbreitung der Krankheit zu stoppen. Mediziner und Experten hoffen, dass diese Maßnahmen den schrecklichen Ausbruch endlich in den Griff bekommen können.", 
        True, 5, 4, 3, "Gesundheit", None),
        
        (11, "Der Londoner Zoo eröffnet neue Ausstellung exotischer Vögel", 
        "Der Londoner Zoo hat eine beeindruckende neue Ausstellung exotischer Vögel eröffnet, die Besucher in Staunen versetzt. Die Sammlung umfasst seltene Arten aus Südamerika und Afrika, die für ihre lebhaften Farben und außergewöhnlichen Gesänge bekannt sind. Ornithologen und Vogelbegeisterte strömten heute zur Eröffnung, um diese gefiederten Schönheiten zu bewundern.", 
        True, 6, 4, 2, "Tiere", None),
        
        (12, "Tiere aus dem fernen Osten: Neue Exoten im Londoner Zoo", 
        "Der Londoner Zoo hat heute eine neue Tierabteilung eröffnet, die sich mit den exotischen Tieren des Fernen Ostens beschäftigt. Besucher können nun den seltenen asiatischen Tiger, den Mandrill und verschiedene Affenarten aus China und Indien bestaunen. Diese Eröffnung wird als Meilenstein in der Erweiterung des Zoos hin zu einem internationaleren Fokus angesehen.", 
        True, 5, 3, 3, "Tiere", None),
        
        (13, "Besondere Attraktion: Das neue Bärengehege im Zoo", 
        "Das neue Bärengehege im Londoner Zoo wurde heute feierlich eröffnet und ist eine der größten Erweiterungen des Zoos in den letzten Jahren. Es beherbergt mehrere Bärenarten, darunter Braunbären und Eisbären, die in einer naturnahen Umgebung leben. Das neue Gehege wurde mit viel Liebe zum Detail gestaltet, um den Tieren das beste Leben zu ermöglichen.", 
        True, 4, 2, 3, "Tiere", None),
        
        (14, "Das Elefantenhaus im Zoo feiert große Neueröffnung", 
        "Der Londoner Zoo feiert die Eröffnung seines neuen Elefantenhauses, das den Tieren mehr Raum und eine besser gestaltete Umgebung bietet. Zwei asiatische Elefanten, die kürzlich aus Indien eingeführt wurden, sind nun die Stars der neuen Anlage. Besucher haben die Möglichkeit, diese majestätischen Tiere in ihrem neuen Zuhause zu beobachten.", 
        True, 6, 4, 2, "Tiere", None),
            
        (1, "Pinguin-Paar im Zoo zeigt erstmals Nachwuchs", 
        "Im Londoner Zoo gibt es guten Grund zur Freude: Ein Pinguin-Paar hat erfolgreich Nachwuchs bekommen. Die ersten Pinguin-Küken des Jahres wurden heute im Aquarienbereich des Zoos vorgestellt. Die Tierpfleger sind stolz auf den Erfolg und hoffen, dass die Küken die wachsende Pinguin-Kolonie im Zoo bereichern werden.", 
        True, None, None, None, "Zoo", None),
        
        (2, "Neue Programme im Zoo zur Förderung des Tierschutzes", 
        "Der Londoner Zoo hat neue Bildungsprogramme ins Leben gerufen, die den Besuchern den Tierschutz näherbringen sollen. Besonders Schülergruppen können an interaktiven Führungen teilnehmen, bei denen sie mehr über den Schutz von bedrohten Tierarten erfahren. Der Zoo hofft, mit diesen Programmen das Bewusstsein für den Erhalt der Artenvielfalt zu schärfen.", 
        True, None, None, None, "Zoo", None),
        
        (3, "Historischer Moment: Der erste Giraffen-Nachwuchs im Zoo", 
        "Im Londoner Zoo wurde ein historischer Moment gefeiert, als die erste Giraffe in der Geschichte des Zoos das Licht der Welt erblickte. Das Neugeborene, ein kleiner Männchen, ist die erste Giraffe, die erfolgreich in Gefangenschaft aufgezogen wurde. Besucher können nun stolz die ersten Schritte des kleinen Giraffenbabys im Gehege beobachten.", 
        True, None, None, None, "Zoo", None),
        
        (4, "Ungewöhnliche Freundschaft im Londoner Zoo: Elefant und Hund", 
        "Eine unerwartete Freundschaft zwischen einem Elefanten und einem Hund im Londoner Zoo hat die Besucher erstaunt. Der Hund, ein Mischling, der vor einigen Monaten als Streuner in den Zoo gebracht wurde, hat sich mit einem der Elefanten angefreundet. Die beiden verbringen nun täglich Zeit miteinander, wobei der Hund dem Elefanten immer wieder zu neuen Streichen anstiftet.", 
        True, None, None, None, "Zoo", None),
        
        (5, "Der mutige Affe – Wie ein Schimpanse einen Zoowärter rettete", 
        "In einer dramatischen Wendung rettete ein Schimpanse namens Max kürzlich das Leben eines Zoowärters. Als der Wärter bei der Pflege des Geheges in einen unbeabsichtigten Kampf mit einem wilden Bären geriet, griff Max ein und lenkte den Bären mit seinen geschickten Bewegungen ab, bis Hilfe eintraf. Der Zoo hat Max für seinen Mut und seine Schnelligkeit in einer feierlichen Zeremonie geehrt.", 
        True, None, None, None, "Zoo", None),
        
        (6, "Große Trauer im Zoo: Der Tod des berühmten Tigermännchens", 
        "Der Londoner Zoo trauert um den Verlust seines bekanntesten Tigers, Rajah, der gestern im Alter von 12 Jahren starb. Rajah, der über die Jahre hinweg zu einem Symbol für den Zoo wurde, war für seine imposante Größe und seinen majestätischen Gang bekannt. Der Tiger hatte zahlreiche Generationen von Besuchern begeistert, und sein Tod hat eine Lücke hinterlassen, die schwer zu füllen ist.", 
        True, None, None, None, "Zoo", None),
        
        (7, "Verblüffende Intelligenz: Ein Papagei löst komplexe Rätsel", 
        "Im Londoner Zoo hat ein Graupapagei namens Albert für Aufsehen gesorgt, als er mehrere komplexe Rätsel löste, die speziell entwickelt wurden, um die Intelligenz von Tieren zu testen. Albert, der für seine außergewöhnliche Fähigkeit, Wörter zu sprechen, bekannt ist, zeigte heute beeindruckende Problemlösungsfähigkeiten, indem er Verschlüsse öffnete und versteckte Leckereien fand. Dieser Erfolg hat das Interesse der wissenschaftlichen Gemeinschaft geweckt.", 
        True, None, None, None, "Zoo", None),
        
        (8, "Die Reise der Giraffe Bella: Ein unvorhergesehener langer Weg nach London", 
        "Die Giraffe Bella, die vor kurzem im Zoo angekommen ist, hatte eine abenteuerliche Reise aus Afrika hinter sich. Aufgrund eines unerwarteten Sturms war der Transportweg ungewöhnlich lang und herausfordernd. Doch Bella zeigte eine bemerkenswerte Resilienz, und trotz der Strapazen kam sie gesund im Zoo an, wo sie nun in einem großen, offenen Gehege mit anderen Giraffen lebt.", 
        True, None, None, None, "Zoo", None),
        
        (9, "Die Rückkehr des seltenen weißen Löwen nach London", 
        "Nach jahrzehntelanger Abwesenheit kehrt ein weißer Löwe nach London zurück. Der seltene Löwe, der von den Zoologen als fast ausgestorben galt, wurde aus Südafrika eingeführt, wo er in einem Schutzgebiet gezüchtet wurde. Der Zoo erhofft sich von seiner Präsenz nicht nur eine Steigerung der Besucherzahlen, sondern auch einen wichtigen Beitrag zum Erhalt der Art.", 
        True, None, None, None, "Zoo", None),
        
        (10, "Der mutige Papagei: Wie ein Vogel die Tür des Geheges öffnete und ausbrach", 
        "Im Londoner Zoo sorgte ein Papagei namens Percy für Chaos, als er eines Tages während seiner Freiflugzeit ein verschlossenes Tor öffnete und fast aus dem Gehege entkommen wäre. Glücklicherweise bemerkten die Zoowärter schnell das Manöver und verhinderten eine Flucht. Der Vorfall hat das Team dazu angeregt, die Sicherheitsmaßnahmen in den Vogelgehegen zu überprüfen.", 
        True, None, None, None, "Zoo", None),
        
        (11, "Bärenbaby im Zoo: Der erste Nachwuchs eines Grizzlypaares", 
        "Ein bedeutendes Ereignis im Londoner Zoo: Ein Grizzlybär-Baby wurde geboren. Dies ist der erste Nachwuchs des Grizzlypaares, das erst vor zwei Jahren im Zoo eingezogen war. Das kleine Bärenbaby, das gesund und kräftig wirkt, zieht bereits die Blicke der Zoobesucher auf sich, und die Pfleger sind optimistisch, dass es gut gedeihen wird.", 
        True, None, None, None, "Zoo", None),
        
        (12, "Die Wunder von Unterwasserwelten: Der erste Oktopus im Zoo", 
        "Der Londoner Zoo hat erstmals einen Oktopus aus den Gewässern vor Südeuropa in einem speziell eingerichteten Aquarium ausgestellt. Der Oktopus, ein wahrer Meister der Tarnung, sorgt für großes Staunen bei den Besuchern, die die erstaunlichen Anpassungsfähigkeiten des Tieres beobachten können. Besonders seine Fähigkeit, sich fast unsichtbar zu machen, fasziniert die Gäste.", 
        True, None, None, None, "Zoo", None),
        
        (13, "Die außergewöhnliche Reise eines Pandas von China nach London", 
        "Der Londoner Zoo hat mit Stolz einen neuen Bewohner empfangen: Ein Riesenpanda, der aus China eingeflogen wurde. Die Reise des Pandas war außergewöhnlich lang und ereignisreich, da mehrere Umstände die Ankunft verzögerten. Nun ist der Panda sicher im Zoo angekommen, und die Zoobesucher können ihn in einem speziell dafür angelegten, naturgetreuen Gehege sehen.", 
        True, None, None, None, "Zoo", None),
        
        (14, "Das neue Aquarium im Londoner Zoo: Ein Fenster in die geheimen Tiefen der Meere", 
        "Heute wurde im Londoner Zoo das brandneue Aquarium eröffnet, das eine faszinierende Unterwasserwelt präsentiert. Die beeindruckende Sammlung umfasst exotische Fische, farbenprächtige Korallenriffe und geheimnisvolle Meerestiere, die sonst nur schwer zugänglich sind. Mit modernster Technik ermöglicht das Aquarium den Besuchern einen einzigartigen Blick auf die Vielfalt und Schönheit der Meere, ohne jemals das Festland verlassen zu müssen. Besonders hervorzuheben sind die riesigen Glaswände, die den Besuchern das Gefühl geben, mitten im Ozean zu schwimmen.", 
        True, None, None, None, "Zoo", None),
            
        (2, "Neuer Roman von Charlotte Brontë: 'Stürme der Leidenschaft'", 
        "Charlotte Brontë, die mit 'Jane Eyre' weltberühmt wurde, veröffentlicht ihr neuestes Werk 'Stürme der Leidenschaft'. Der Roman erzählt die Geschichte von Lady Eveline, die gegen ihre eigenen inneren Konflikte und gesellschaftliche Erwartungen ankämpft. Leserinnen dürfen sich auf die bewährte Mischung aus tiefgründiger Charakterentwicklung und leidenschaftlicher Romantik freuen.", 
        True, 4, 3, 3, "Literatur", None),
        
        (3, "Emma Woodhouse: Die Rückkehr in die Welt von Jane Austen", 
        "Eine neue Ausgabe von Jane Austens zeitlosem Klassiker 'Emma' wurde gerade veröffentlicht, die nun in einer erweiterten Version mit zusätzlichen Briefen und Gedanken der Autorin erscheint. Diese neue Fassung gibt tiefe Einblicke in die Gedankenwelt der jungen Emma und ihre romantischen Verstrickungen. Ein Muss für alle Austen-Liebhaberinnen.", 
        True, 5, 2, 3, "Literatur", None),
        
        (4, "Die geheime Dame: Ein spannender Roman von Mary Shelley", 
        "Mary Shelley, bekannt für 'Frankenstein', überrascht mit ihrem neuesten Werk 'Die geheime Dame'. Es ist ein dramatischer Roman über die starke, aber geheimnisvolle Lady Veronica, die in einer Zeit des gesellschaftlichen Umbruchs ihr eigenes Schicksal in die Hand nimmt. Ein packender Mix aus Spannung und gesellschaftlicher Kritik.", 
        True, 6, 4, 4, "Literatur", None),
        
        (5, "Sophie’s Wahl: Neue Erzählung von Elizabeth Gaskell", 
        "In ihrem neuesten Roman 'Sophie’s Wahl' beleuchtet Elizabeth Gaskell die inneren Kämpfe einer jungen Frau im viktorianischen England. Sophie, eine einfache junge Dame, muss sich zwischen zwei unterschiedlichen Männern und einer unmöglichen Liebe entscheiden. Gaskells typischer Gesellschaftsroman trifft auf rührende Herzensangelegenheiten.", 
        True, 3, 5, 3, "Literatur", None),
        
        (6, "Die Blumen des Herzens: Ein Liebesroman von Louisa May Alcott", 
        "Louisa May Alcott, die Schöpferin von 'Little Women', hat mit 'Die Blumen des Herzens' ein weiteres Meisterwerk der Romantik geschrieben. In dieser Geschichte geht es um die junge Amy, die sich zwischen der Liebe zu einem alten Freund und einem neuen Verehrer entscheiden muss. Ein herzergreifender Roman, der die Grenzen zwischen Pflicht und Liebe auslotet.", 
        True, 7, 2, 3, "Literatur", None),
        
        (7, "Verborgene Sehnsüchte: Ein neuer Roman von Anne Brontë", 
        "Mit 'Verborgene Sehnsüchte' zeigt Anne Brontë eine romantische, aber auch tiefgründige Geschichte über eine junge Frau, die in der gelebten Pflicht der Gesellschaft ihre eigenen Wünsche und Sehnsüchte verbirgt. Ein emotionaler Roman über das Streben nach Glück in einer Welt der Konventionen.", 
        True, 4, 3, 3, "Literatur", None),
        
        (8, "Herz und Verstand: Ein Bestseller von Julia Kavanagh", 
        "Julia Kavanagh bringt uns in ihrem neuesten Werk 'Herz und Verstand' die Geschichte einer jungen Frau, die versucht, ihre Leidenschaft für einen unerreichbaren Mann mit ihrer Pflicht als Tochter und Schwester in Einklang zu bringen. Ein fesselnder Roman über die Komplexität von Entscheidungen im Leben einer Frau.", 
        True, 2, 4, 3, "Literatur", None),
        
        (9, "Der Zauber der Nacht: Ein mystischer Roman von Sarah Doudney", 
        "Sarah Doudney überrascht mit ihrem neuesten Werk 'Der Zauber der Nacht', in dem eine junge Frau mit übernatürlichen Kräften in die Wirren eines geheimen Zirkels von Zauberern gerät. Eine Mischung aus Romantik, Magie und mystischen Geheimnissen, die alle Erwartungen an einen Frauenroman übertreffen.", 
        True, 5, 3, 4, "Literatur", None),
        
        (10, "Im Schatten des Hauses: Ein neuer Roman von Wilkie Collins", 
        "Obwohl Wilkie Collins vor allem für seine Kriminalromane bekannt ist, wagt er sich mit 'Im Schatten des Hauses' an ein vielschichtiges Drama über eine junge Frau, die gegen die Intrigen einer mächtigen Familie kämpfen muss. Ein fesselnder und packender Roman, der Geheimnisse, Leidenschaft und Verrat miteinander verbindet.", 
        True, 6, 4, 3, "Literatur", None),
        
        (11, "Das silberne Band: Ein Historienroman von Emily Brontë", 
        "Emily Brontë begeistert mit 'Das silberne Band' – einer Geschichte von Liebe, Verlust und der erlösenden Kraft der Zeit. Der Roman spielt im viktorianischen England und erzählt von der geheimen Liebe einer jungen Dame und dem Mann, der sie durch ein tragisches Schicksal entfremdet hat.", 
        True, 7, 3, 3, "Literatur", None),
        
        (12, "Der Schatz der verlorenen Stadt: Ein Abenteuerroman von Jules Verne", 
        "Jules Verne entführt seine Leser in 'Der Schatz der verlorenen Stadt' in die entlegenen Dschungel Südamerikas, wo ein mutiger Archäologe nach einem sagenumwobenen Schatz sucht. Spannung, Gefahr und aufregende Entdeckungen erwarten den Leser in diesem packenden Abenteuerroman.", 
        True, 8, 4, 3, "Abenteuer", None),
        
        (13, "Der Graf von Monte Cristo: Die neue Ausgabe von Alexandre Dumas", 
        "Alexandre Dumas bringt mit 'Der Graf von Monte Cristo' einen seiner größten Klassiker in einer neuen, erweiterten Ausgabe heraus. Dieses epische Werk über Rache, Verrat und Gerechtigkeit bleibt eine der fesselndsten Geschichten der französischen Literatur.", 
        True, 5, 2, 4, "Literatur", None),
        
        (14, "Der letzte Samurai: Ein historischer Thriller von James Clavell", 
        "James Clavell präsentiert in 'Der letzte Samurai' einen packenden historischen Thriller, der die Reise eines europäischen Kriegers im feudalen Japan verfolgt. Die Geschichte von Kampf, Ehre und Aufopferung wird von seinen Lesern mit Spannung erwartet.", 
        True, 7, 3, 3, "Thriller", None),
        
        (15, "Schwermetall: Ein Abenteuer von Robert Louis Stevenson", 
        "Robert Louis Stevenson überrascht mit seinem neuen Abenteuerroman 'Schwermetall', in dem ein erfahrener Seemann auf einem geheimen, verschollenen Schiff nach Schätzen sucht. Spannung, Gefahr und dunkle Geheimnisse sind garantiert.", 
        True, 6, 4, 3, "Abenteuer", None),
        
        (16, "Das Geheimnis des Turms: Ein Kriminalroman von Edgar Allan Poe", 
        "Edgar Allan Poe, der Meister des düsteren Erzählens, veröffentlicht mit 'Das Geheimnis des Turms' einen neuen Kriminalroman. In einer mysteriösen und düsteren Stadt löst ein Privatdetektiv einen geheimen Mordfall auf, der in die tiefsten Abgründe der menschlichen Psyche führt.", 
        True, 4, 2, 4, "Krimi", None),
        
        (17, "Jagd auf den schwarzen Panther: Ein Abenteuer von H. Rider Haggard", 
        "H. Rider Haggard, bekannt für seine Abenteuerromane, veröffentlicht 'Jagd auf den schwarzen Panther'. Der Roman folgt einem mutigen Jäger, der in den afrikanischen Dschungel aufbricht, um ein legendäres, gefährliches Tier zu fangen. Spannung, Nervenkitzel und exotische Schauplätze erwarten die Leser.", 
        True, 6, 3, 4, "Abenteuer", None),
            
        (1, "Die Männer der Nacht: Ein Thriller von Bram Stoker", 
        "Bram Stoker, der mit 'Dracula' berühmt wurde, bringt mit 'Die Männer der Nacht' einen spannenden Thriller heraus, der von einem geheimen Orden handelt, der das Leben einer Stadt in dunklen Geheimnissen und Machenschaften steuert. Ein faszinierendes und packendes Buch, das den Atem anhalten lässt.", 
        True, 4, 3, 3, "Thriller", None),
        
        (2, "Der verborgene Pfad: Ein historischer Roman von Sir Arthur Conan Doyle", 
        "Sir Arthur Conan Doyle stellt mit 'Der verborgene Pfad' einen historischen Thriller vor, der in der viktorianischen Ära spielt. Ein Ermittler begibt sich auf die Spur eines rätselhaften Verbrechens, das tief in die Geheimnisse einer vergangenen Zeit führt.", 
        True, 4, 3, 3, "Historischer Roman", None),
        
        (3, "Der fliegende Mann: Ein Science-Fiction-Roman von H.G. Wells", 
        "H.G. Wells veröffentlicht mit 'Der fliegende Mann' einen aufregenden Science-Fiction-Roman, in dem ein Erfinder in den Lüften schwebt und auf unerforschte Gebiete der Luftfahrt stößt. Der Roman kombiniert aufregende Erfindungen und tiefgehende Fragen zur menschlichen Natur.", 
        True, 4, 3, 3, "Science-Fiction", None),
        
        (4, "Im Sog des Sturms: Ein Abenteuer von Joseph Conrad", 
        "Joseph Conrad bringt mit 'Im Sog des Sturms' einen packenden Abenteuerroman über das Leben auf hoher See. Der Roman erzählt von einem Kapitän, der gegen Naturgewalten und menschliche Fehler kämpft, um ein großes Handelsimperium zu retten.", 
        True, 4, 3, 3, "Abenteuer", None),
        
        (5, "Die Gesellschaft im Wandel: Ein neues Werk von John Stuart Mill", 
        "Der einflussreiche Philosoph John Stuart Mill veröffentlicht mit 'Die Gesellschaft im Wandel' eine eingehende Analyse der Veränderungen in der britischen Gesellschaft im 19. Jahrhundert. Er beleuchtet den Einfluss von Freiheit und Gerechtigkeit auf die soziale Struktur und gibt tiefgehende Einsichten in die britische Kultur der Zeit.", 
        True, 4, 3, 3, "Philosophie", None),
        
        (6, "Die Kunst der Mode: Ein Sachbuch von Elizabeth Tuckerman", 
        "Elizabeth Tuckerman gibt in ihrem neuen Werk 'Die Kunst der Mode' Einblicke in die viktorianische Mode und deren gesellschaftliche Bedeutung. Sie beschreibt, wie Kleidung als Ausdruck von Status und gesellschaftlicher Zugehörigkeit dient und die Entwicklung der Mode im 19. Jahrhundert.", 
        True, 4, 3, 3, "Sachbuch", None),
        
        (7, "Industrie und Mensch: Die soziale Frage im viktorianischen England", 
        "In 'Industrie und Mensch' untersucht der Sozialwissenschaftler Edward Gibbon die Auswirkungen der industriellen Revolution auf die soziale Struktur Englands. Ein tiefgründiges Werk, das die Entstehung von Armutsvierteln und die wachsende Kluft zwischen Arm und Reich beleuchtet.", 
        True, 4, 3, 3, "Soziologie", None),
        
        (8, "Kunst und Gesellschaft: Eine kritische Betrachtung von Walter Pater", 
        "Walter Pater analysiert in 'Kunst und Gesellschaft' den Einfluss von Kunst auf die Gesellschaft des 19. Jahrhunderts. Er erforscht, wie sich der Geschmack und die Wahrnehmung von Kunst im Zuge von gesellschaftlichen Veränderungen entwickelt haben.", 
        True, 4, 3, 3, "Kunst", None),
        
        (9, "Das viktorianische Familienleben: Ein Buch von Fanny Fern", 
        "Fanny Fern, die bereits mit vielen ihrer Schriften die Frauenbewegung unterstützte, veröffentlicht 'Das viktorianische Familienleben'. Sie geht auf die gesellschaftlichen Normen und Herausforderungen ein, denen Frauen und Kinder im England des 19. Jahrhunderts ausgesetzt sind.", 
        True, 4, 3, 3, "Gesellschaft", None),
        
        (10, "Der Blick auf den Kolonialismus: Eine Studie von Richard Burton", 
        "Der Forscher und Entdecker Richard Burton veröffentlicht ein umfassendes Werk über den britischen Kolonialismus und seine Auswirkungen auf die Kultur der eroberten Völker. 'Der Blick auf den Kolonialismus' beleuchtet den britischen Einfluss auf Afrika, Asien und den Nahen Osten.", 
        True, 4, 3, 3, "Historische Studie", None),
        
        (11, "Die revolutionären Ideen: Eine Analyse von Karl Marx", 
        "Karl Marx bringt mit seinem neuesten Werk 'Die revolutionären Ideen' eine tiefgreifende Analyse der sozialen und politischen Revolutionen in Europa. Marx untersucht die Ursachen von Armut und Ausbeutung und schlägt Lösungen vor, die die Grundlage für moderne sozialistische Bewegungen legen.", 
        True, 4, 3, 3, "Politik", None),
        
        (12, "Die Bedeutung von Literatur im viktorianischen Zeitalter", 
        "In diesem Werk untersucht der Literaturkritiker Edmund Gosse, wie die Literatur des viktorianischen Zeitalters die gesellschaftlichen Normen und das Selbstverständnis der Briten beeinflusste. Ein fundierter Blick auf die Entwicklung der Literatur und ihre Rolle in der viktorianischen Kultur.", 
        True, 4, 3, 3, "Literatur", None),
        
        (13, "Philosophie und Religion im 19. Jahrhundert: Ein Buch von Thomas Carlyle", 
        "Thomas Carlyle diskutiert in seinem neuen Werk 'Philosophie und Religion im 19. Jahrhundert' die zunehmende Bedeutung von Philosophie und Religion für die viktorianische Gesellschaft. Er setzt sich kritisch mit den religiösen und philosophischen Strömungen dieser Zeit auseinander und fordert eine tiefere Reflexion über Glaube und Vernunft.", 
        True, 4, 3, 3, "Philosophie und Religion", None),
        
        (14, "Die Entwicklung des Feminismus: Ein Buch von Harriet Martineau", 
        "Harriet Martineau, eine der ersten feministischen Denkerinnen des 19. Jahrhunderts, präsentiert in ihrem Werk 'Die Entwicklung des Feminismus' die Ursprünge der Frauenbewegung und deren Einfluss auf die gesellschaftlichen Veränderungen der Epoche.", 
            True, 4, 3, 3, "Feminismus", None),
            
        (1, "Neue Dampfschiffgesellschaft in London gegründet", 
        "Die 'Royal Steam Navigation Company' hat heute ihre Gründung bekannt gegeben. Mit einer Flotte moderner Dampfschiffe wird die Gesellschaft den Fracht- und Passagierverkehr zwischen Großbritannien und den Vereinigten Staaten revolutionieren. Die ersten Schiffe werden bereits im kommenden Jahr erwartet.", 
        True, 4, 3, 3, "Wirtschaft", None),
        
        (2, "Innovative Maschinenfabrik von Charles H. Ford eröffnet", 
        "Charles H. Ford hat heute seine neue Maschinenfabrik in Manchester eröffnet. Die Firma wird sich auf die Herstellung von Maschinen für die Textilindustrie spezialisieren und erwartet, die Produktionsprozesse durch innovative Technologien zu optimieren. Ford verspricht, Arbeitsplätze in der Region zu schaffen und die Industrie zu modernisieren.", 
        True, 4, 3, 3, "Industrie", None),
        
        (3, "Erste Eröffnung von Londons neuer Teefirma", 
        "Die 'Imperial Tea Company' hat ihre erste Filiale in London eröffnet und bietet eine breite Auswahl an hochwertigen Teesorten aus Indien und China an. Gründerin Alice McNeil betont, dass ihre Firma besonderen Wert auf die Qualität und Nachhaltigkeit ihrer Produkte legt.", 
        True, 4, 3, 3, "Unternehmen", None),
        
        (4, "Stahlgigant 'Blackstone & Co.' expandiert nach Amerika", 
        "'Blackstone & Co.', einer der führenden Stahlhersteller in Großbritannien, hat heute seine Expansion in die Vereinigten Staaten bekannt gegeben. Durch den Bau eines neuen Stahlwerks in Pittsburgh will das Unternehmen die steigende Nachfrage nach Eisen und Stahl in Nordamerika bedienen.", 
        True, 4, 3, 3, "Wirtschaft", None),
        
        (5, "Dampflok-Hersteller 'Victoria Locomotives' auf Erfolgskurs", 
        "'Victoria Locomotives', ein führender Hersteller von Dampflokomotiven, hat einen neuen Rekord für den Absatz seiner Lokomotiven aufgestellt. Die Firma hat Verträge mit mehreren großen Eisenbahngesellschaften unterzeichnet, um die neuesten Modelle zu liefern, die für ihre Effizienz und Leistungsfähigkeit bekannt sind.", 
        True, 4, 3, 3, "Industrie", None),
        
        (6, "Die 'Royal Crystal Glassworks' liefert Glaswaren für die Queen", 
        "Die 'Royal Crystal Glassworks' hat bekannt gegeben, dass sie exklusiver Lieferant von Kristallglaswaren für den königlichen Haushalt geworden ist. Das Unternehmen ist stolz auf die Anerkennung seiner Kunstfertigkeit und erwartet nun einen Anstieg der Nachfrage nach seinen luxuriösen Produkten.", 
        True, 4, 3, 3, "Luxusgüter", None),
        
        (7, "Erste Parfümfabrik von Lady Eveline eröffnet", 
        "Lady Eveline Albright hat in London ihre erste Parfümfabrik eröffnet, die sich auf die Herstellung hochwertiger, einzigartiger Düfte spezialisiert. Die Fabrik plant, einen revolutionären Duft zu produzieren, der die Welt der Parfümerie auf den Kopf stellen soll.", 
        True, 4, 3, 3, "Unternehmen", None),
        
        (8, "Londoner Schuhfabrik steigert Produktion durch neue Technologie", 
        "Die 'West End Shoe Factory' hat kürzlich in neue Maschinen investiert, die die Schuhproduktion erheblich steigern sollen. Die Firma erwartet, durch die Einführung dieser neuen Technologien die führende Marke für hochwertiges Schuhwerk in London zu werden.", 
        True, 4, 3, 3, "Industrie", None),
        
        (9, "Erfolgreiche Erweiterung der 'Global Printing Press'", 
        "Die Druckerei 'Global Printing Press' hat ihre Kapazitäten erheblich erweitert und ist nun in der Lage, Zeitschriften und Bücher in größerem Umfang zu produzieren. Mit der neuesten Technik und einem qualifizierten Team von Fachleuten hofft das Unternehmen, die größten Verlage Englands zu bedienen.", 
        True, 4, 3, 3, "Druckindustrie", None),
        
        (10, "Eisenwarenladen von William Thompson gewinnt großen Vertrag", 
        "William Thompson, ein Londoner Eisenwarenhändler, hat einen bedeutenden Vertrag mit der britischen Armee abgeschlossen, um militärische Ausrüstungen zu liefern. Die Vereinbarung stärkt Thompson's Ruf als vertrauenswürdiger Lieferant von hochqualitativen Eisenwaren und Ausstattungen.", 
        True, 4, 3, 3, "Wirtschaft", None),
        
        (11, "Neue Textilfabrik von 'Windsor Mills' nimmt Produktion auf", 
        "Die 'Windsor Mills' haben heute ihre neue Textilfabrik eröffnet, die nun mit modernsten Webmaschinen ausgestattet ist. Der Geschäftsführer, Sir Reginald Turner, kündigte an, dass die Fabrik hochwertige Stoffe für die wachsende Modeindustrie herstellen wird.", 
        True, 4, 3, 3, "Textilindustrie", None),
        
        (12, "Automobilhersteller 'Regal Motors' revolutioniert den Markt", 
        "'Regal Motors' hat das erste funktionierende Automobil auf den Markt gebracht und wird für seine bahnbrechende Technologie gefeiert. Das Unternehmen, das in den letzten Monaten immense Investitionen getätigt hat, stellt nun die ersten Modelle für wohlhabende britische Käufer her.", 
        True, 4, 3, 3, "Automobilindustrie", None),
        
        (13, "Neue Dampfbäckerei von 'Golden Loaf' revolutioniert die Produktion", 
        "Die Firma 'Golden Loaf' hat eine Dampfbäckerei eröffnet, die es ihr ermöglicht, Brot und Gebäck in großen Mengen zu produzieren. Dank moderner Dampftechnologie wird eine gleichbleibend hohe Qualität gewährleistet und die Produktion erhöht.", 
        True, 4, 3, 3, "Lebensmittelindustrie", None),
        
        (14, "Telegraphenfirma 'Transcontinental Lines' erzielt Durchbruch", 
        "'Transcontinental Lines', ein führendes Unternehmen in der Telegraphenbranche, hat einen bedeutenden Fortschritt bei der Schaffung eines landesweiten Telegraphennetzwerks erzielt. Das Unternehmen strebt an, die Kommunikationsmöglichkeiten in Großbritannien und darüber hinaus zu revolutionieren.", 
            True, 4, 3, 3, "Kommunikation", None),
            
        (1, "Neue Brauerei 'Westminster Brewing' in London eröffnet", 
        "Die neue Brauerei 'Westminster Brewing' hat heute ihren Betrieb aufgenommen und stellt bereits eine Reihe erfrischender Biere her. Ihr Ziel ist es, nicht nur lokale Märkte zu beliefern, sondern auch international Anerkennung für ihre Braukunst zu gewinnen.", 
        True, 4, 3, 3, "Getränkeindustrie", None),
        
        (2, "Medizinisches Unternehmen 'Royal Health Co.' bringt neue Behandlungsmethoden auf den Markt", 
        "Die 'Royal Health Co.' hat neue medizinische Behandlungen und Technologien entwickelt, die eine bahnbrechende Wirkung auf die Heilung von Infektionskrankheiten haben sollen. Experten und Mediziner sind von den Fortschritten beeindruckt, die die Behandlungsmöglichkeiten revolutionieren könnten.", 
        True, 4, 3, 3, "Gesundheitswesen", None),
        
        (3, "Elektronikfirma 'Future Innovations' stellt bahnbrechendes Gerät vor", 
        "Die 'Future Innovations' haben auf der jährlichen Technologiemesse ein bahnbrechendes Gerät vorgestellt, das als erster elektrischer Haushaltshelfer gilt. Der neuartige Apparat verspricht, den Alltag der Menschen zu erleichtern und das Leben deutlich zu vereinfachen.", 
        True, 4, 3, 3, "Technologie", None),
        
        (4, "Große Expansion für die 'Royal Shipping Company'", 
        "Die 'Royal Shipping Company' hat bekannt gegeben, dass sie ihre Flotte um zehn neue Schiffe erweitern wird, um den internationalen Handel mit Kolonien und Überseegebieten zu fördern. Dies ist ein Schritt, der die Wettbewerbsfähigkeit der Firma auf dem Weltmarkt stärken wird.", 
        True, 4, 3, 3, "Transport", None),
        
        (5, "Eröffnung des 'Sovereign Jewelers' in der Londoner City", 
        "Das renommierte Schmuckgeschäft 'Sovereign Jewelers' hat eine neue Filiale in der Londoner City eröffnet und bietet exklusive Kollektionen von Diamanten und Edelsteinen an. Das Geschäft hat sich auf edelste Materialien und handgefertigte Schmuckstücke spezialisiert.", 
        True, 4, 3, 3, "Luxusgüter", None),
        
        (6, "Innovative Möbelherstellung bei 'London Upholstery Co.'", 
        "Die 'London Upholstery Co.' hat ihre Produktionsmethoden modernisiert und neue Möbelkollektionen vorgestellt, die Design und Komfort vereinen. Das Unternehmen setzt auf den Einsatz von hochwertigen Stoffen und innovativen Polstertechniken, um sich von der Konkurrenz abzuheben.", 
        True, 4, 3, 3, "Möbelindustrie", None),
        
        (7, "Eisenbahnfirma 'Great Western Railway' baut neue Strecke", 
        "Die 'Great Western Railway' hat bekannt gegeben, dass sie eine neue Zugstrecke zwischen London und Bristol eröffnen wird. Diese Erweiterung soll den Handel und den Personentransport erheblich erleichtern und gleichzeitig die Wirtschaft in der Region ankurbeln.", 
        True, 4, 3, 3, "Transport", None),
        
        (8, "Bücherverlag 'Pen & Quill' führt neues Abonnement-Modell ein", 
        "Der Londoner Verlag 'Pen & Quill' führt ein neues Abonnement-Modell ein, das es Lesern ermöglicht, regelmäßig die neuesten Romane und Literaturwerke zu erhalten. Das Modell soll besonders die Nachfrage nach literarischen Neuerscheinungen steigern und Leser in Großbritannien und darüber hinaus erreichen.", 
        True, 4, 3, 3, "Verlag", None),
        
        (9, "Die 'Sapphire Textile Mills' erweitern ihre Produktionskapazitäten", 
        "'Sapphire Textile Mills' haben die Eröffnung einer neuen Spinnerei gefeiert, die die Produktionskapazitäten des Unternehmens verdoppeln wird. Die Fabrik wird vor allem Stoffe für die Modeindustrie produzieren und soll das Unternehmen zum führenden Anbieter in der Region machen.", 
        True, 4, 3, 3, "Textilindustrie", None),
        
        (10, "Handelsgesellschaft 'East India Trading Co.' erweitert Marktanteile", 
        "Die 'East India Trading Co.' hat einen neuen Vertrag mit indischen Lieferanten abgeschlossen und wird bald eine größere Auswahl an Gewürzen, Seide und Tee nach Großbritannien importieren. Diese Expansion wird die Firma zum führenden Handelsunternehmen im internationalen Markt machen.", 
        True, 4, 3, 3, "Handel", None),
        
        (11, "Kunststofffabrik 'Bright Future Ltd.' revolutioniert Verpackungsindustrie", 
        "'Bright Future Ltd.' hat eine innovative Kunststofftechnologie entwickelt, die die Verpackungsindustrie verändern könnte. Die neue Methode verspricht, die Haltbarkeit von Produkten zu verlängern und gleichzeitig die Herstellungskosten zu senken.", 
        True, 4, 3, 3, "Industrie", None),
        
        (12, "Die 'Royal Brewing Company' startet Produktion von Malzbier", 
        "Die 'Royal Brewing Company' hat heute die Produktion von Malzbier aufgenommen, das als alkoholfreie Alternative zu herkömmlichem Bier erhältlich sein wird. Das Unternehmen erwartet eine hohe Nachfrage, da immer mehr Menschen nach gesünderen Getränken suchen.", 
        True, 4, 3, 3, "Getränkeindustrie", None),
        
        (13, "Neue 'Aero Aviation Co.' will Luftfahrt revolutionieren", 
        "Die 'Aero Aviation Co.' hat ein innovatives neues Flugzeugmodell entwickelt, das kürzere Reisezeiten und geringeren Treibstoffverbrauch verspricht. Das Unternehmen plant, in den kommenden Jahren die ersten Passagierflüge anzubieten und die Luftfahrtindustrie zu verändern.", 
        True, 4, 3, 3, "Luftfahrt", None),
        
        (14, "Bau von 'New London Docks' durch 'Harbor Engineering Co.'", 
        "'Harbor Engineering Co.' hat den Bau der 'New London Docks' abgeschlossen, die den internationalen Handel durch eine moderne Hafeninfrastruktur erleichtern werden. Der neue Hafen soll sowohl den Import als auch den Export von Waren erheblich steigern.", 
        True, 4, 3, 3, "Transport", None),
        
        (15, "Die 'Greenwood Forestry Co.' startet nachhaltige Holzproduktion", 
        "Die 'Greenwood Forestry Co.' hat bekannt gegeben, dass sie nun auf eine nachhaltige Methode der Holzernte umstellt. Das Unternehmen wird Wälder nach den Prinzipien der Wiederaufforstung bewirtschaften und erwartet, dass dies sowohl der Umwelt als auch der Wirtschaft zugutekommt.", 
            True, 4, 3, 3, "Forstwirtschaft", None),
                
        (1, "Londoner Pferderennsaison bringt spannende Rennen", 
        "Die aktuelle Pferderennsaison in London hat mit aufregenden Wettkämpfen auf den renommierten Rennbahnen von Ascot und Newmarket begonnen. Viele Favoriten konnten ihren Ruf bestätigen, doch auch einige Außenseiter überraschten mit beeindruckenden Leistungen. Die nächste große Veranstaltung ist bereits in Planung.", 
        True, 4, 3, 3, "Sport", None),
        
        (2, "Der FC London gewinnt erneut gegen die Bristol Rovers", 
        "Der FC London hat seine hervorragende Form in der laufenden Saison fortgesetzt und besiegte die Bristol Rovers mit 3:1. Die Londoner zeigten eine exzellente Teamleistung, besonders in der zweiten Halbzeit, und sichern sich damit weitere wichtige Punkte in der Tabelle.", 
        True, 4, 3, 3, "Sport", None),
        
        (3, "Cricket-Team von Lancashire triumphiert im Derby gegen Yorkshire", 
        "Das Cricket-Team von Lancashire setzte sich in einem packenden Derby gegen Yorkshire mit 8 Wickets durch. Besonders herausragend war der Schlagmann Jonathan Price, der mit 125 Runs einen entscheidenden Beitrag zum Sieg leistete.", 
        True, 4, 3, 3, "Sport", None),
        
        (4, "Stormwind sichert sich den Sieg im Royal Derby", 
        "Das Pferd 'Stormwind' von Züchter William Redford hat erneut das Royal Derby gewonnen und seine Dominanz auf den Rennbahnen unter Beweis gestellt. Viele Experten sehen in dem Sieg ein Zeichen für die außergewöhnliche Qualität des Zuchtpferdes und seiner Vorbereitung.", 
        True, 4, 3, 3, "Sport", None),
        
        (5, "Manchester Rugby Club triumphiert in der Nationalen Liga", 
        "Der Manchester Rugby Club konnte einen überzeugenden Sieg in der Nationalen Liga feiern und festigte seinen Platz an der Tabellenspitze. Mit einem 7:0-Sieg gegen das Team aus Liverpool bleibt Manchester das stärkste Team der Liga.", 
        True, 4, 3, 3, "Sport", None),
        
        (6, "Jack Thompson verteidigt erfolgreich seinen Boxtitel", 
        "Boxweltmeister Jack Thompson konnte seinen Titel in einem spannungsgeladenen Kampf gegen Herausforderer Samuel 'Iron Fist' Turner verteidigen. Nach 12 harten Runden erzielte Thompson einen einstimmigen Punktsieg und bleibt weiterhin ungeschlagen.", 
        True, 4, 3, 3, "Sport", None),
        
        (7, "Tennis-Club London zieht internationales Interesse an", 
        "Der Tennis-Club London hat durch seine herausragende Organisation und das hohe Niveau seiner Turniere internationale Aufmerksamkeit auf sich gezogen. Zahlreiche renommierte Spieler aus Frankreich, Deutschland und den Niederlanden haben ihre Teilnahme an den kommenden Meisterschaften bestätigt.", 
        True, 4, 3, 3, "Sport", None),
        
        (8, "Etablierter Fußballverein 'Arsenal' gewinnt auswärts gegen Sheffield United", 
        "Der Fußballverein Arsenal feierte einen klaren 4:1-Sieg in Sheffield und setzte sich damit weiter an die Spitze der Tabelle. Besonders der junge Stürmer Harry Dawson zeigte sich in bestechender Form und erzielte zwei Tore.", 
        True, 4, 3, 3, "Sport", None),
        
        (9, "Segler aus London gewinnen international renommiertes Rennen", 
        "Die Londoner Segler haben das berühmte Rennen von Cowes gewonnen und das britische Team erneut an die Spitze der internationalen Segelwettkämpfe geführt. Besonders das strategische Geschick der Crew war entscheidend für den Erfolg.", 
        True, 4, 3, 3, "Sport", None),
        
        (10, "Das Edinburgh Rugby-Team bleibt ungeschlagen", 
        "Das Rugby-Team aus Edinburgh bleibt auch nach der letzten Begegnung mit einem klaren 9:0-Sieg gegen Cardiff ungeschlagen. Die Schotten setzen ihre beeindruckende Serie fort und haben nun einen komfortablen Vorsprung in der Tabelle.", 
        True, 4, 3, 3, "Sport", None),
        
        (11, "Der 'Golden Glove' Box-Wettbewerb bleibt spannend", 
        "Der 'Golden Glove'-Boxwettbewerb bleibt eines der spannendsten Events des Jahres. Nach mehreren dramatischen Kämpfen stehen nun die Halbfinals bevor, und die britische Boxszene erwartet mit Spannung, wer den begehrten Titel holen wird.", 
        True, 4, 3, 3, "Sport", None),
        
        (12, "Londoner Cricket-Team besiegt Kent im entscheidenden Spiel", 
        "Das Londoner Cricket-Team konnte einen wichtigen Sieg gegen Kent verbuchen und setzte sich mit 5 Wickets durch. Der herausragende Bowler William Harris erzielte entscheidende Wickets und sicherte seinem Team den Sieg.", 
        True, 4, 3, 3, "Sport", None),
        
        (13, "Gewichtheben: Der britische Champion stellt neuen Rekord auf", 
        "Der Gewichtheber Thomas Williams hat im aktuellen Wettbewerb einen neuen britischen Rekord im Reißen aufgestellt. Mit einer Leistung von 160 Kilogramm im Gewichtheben setzte er sich an die Spitze und löste Begeisterung bei den Anhängern aus.", 
        True, 4, 3, 3, "Sport", None),
        
        (14, "Rugby-Team aus Wales besiegt Irland in hart umkämpftem Spiel", 
        "Das walisische Rugby-Team setzte sich in einem spannenden und hart umkämpften Spiel mit 12:9 gegen Irland durch. Die walisischen Spieler zeigten sowohl in der Verteidigung als auch im Angriff eine hervorragende Leistung.", 
        True, 4, 3, 3, "Sport", None),
        
        (15, "Boxkampf zwischen Londoner und New Yorker Herausforderern endet unentschieden", 
        "Der internationale Boxkampf zwischen dem Londoner Champion Thomas White und dem New Yorker Herausforderer William Johnson endete nach zwölf spannungsgeladenen Runden mit einem Unentschieden. Beide Boxer zeigten ihr Können, doch ein klarer Sieger konnte nicht ermittelt werden.", 
        True, 4, 3, 3, "Sport", None),
            
        (1, "Hochklassiger Wettkampf im Londoner Tennis-Club", 
        "Der Tennis-Wettbewerb im Londoner Tennis-Club setzte neue Maßstäbe in Sachen Spielniveau. Der englische Spieler Edward Green konnte den Titel in einem dramatischen Finale gegen den Amerikaner Henry Johnson gewinnen und somit sein Können unter Beweis stellen.", 
        True, 4, 3, 3, "Sport", None),
        
        (2, "Der FC London setzt sich in der Liga klar durch", 
        "Der FC London zeigt in dieser Saison eine beeindruckende Leistung und sicherte sich mit einem weiteren 2:0-Sieg gegen Nottingham Forest drei wichtige Punkte. Die Londoner Mannschaft bleibt weiterhin das Maß aller Dinge in der Liga.", 
        True, 4, 3, 3, "Sport", None),
        
        (3, "Golfturnier in Edinburgh zieht prominente Spieler an", 
        "Das jährliche Golfturnier in Edinburgh hat erneut eine Vielzahl von prominenten Spielern aus dem ganzen Land angezogen. Besonders die Duelle zwischen den schottischen und englischen Spielern sorgten für viel Aufsehen und Spannung.", 
        True, 4, 3, 3, "Sport", None),
        
        (4, "Manchester City und Liverpool liefern sich packendes Fußball-Duell", 
        "In einem der spannendsten Fußballspiele der Saison trennten sich Manchester City und Liverpool mit einem 2:2-Unentschieden. Beide Teams zeigten spektakuläre Leistungen und lieferten sich über 90 Minuten einen heißen Kampf um die Tabellenführung.", 
        True, 4, 3, 3, "Sport", None),
        
        (5, "Leichtathletik-Wettbewerb in London sorgt für Rekorde", 
        "Der Leichtathletik-Wettbewerb in London brachte zahlreiche neue Rekorde. Besonders in den Disziplinen 100 Meter und Weitsprung gab es beeindruckende Leistungen, die die Zuschauer begeisterten und die Athleten zu neuen Bestleistungen antrieben.", 
        True, 4, 3, 3, "Sport", None),
        
        (6, "Neuer Tennisstar aus Liverpool erobert die Turniere", 
        "Der junge Tennisspieler George Harrison aus Liverpool hat sich in den letzten Wochen bei mehreren Turnieren durchgesetzt und wird nun als eines der vielversprechendsten Talente des Landes gefeiert. Seine Leistung gegen den ehemaligen Champion David Black war besonders beeindruckend.", 
        True, 4, 3, 3, "Sport", None),
        
        (7, "Segler aus Edinburgh gewinnen das Jahresrennen", 
        "Das Team aus Edinburgh hat das Jahresrennen in der Segelklasse A gewonnen und sich mit einer perfekten Strategie den ersten Platz gesichert. Das Team zeigte außergewöhnliche Präzision bei der Navigation und setzte sich knapp vor den Londoner Seglern durch.", 
        True, 4, 3, 3, "Sport", None),
        
        (8, "Londoner Cricket-Team dominiert den Wettbewerb in Birmingham", 
        "Das Londoner Cricket-Team hat das diesjährige Turnier in Birmingham mit einer beeindruckenden Gesamtleistung gewonnen. Besonders die beiden Starspieler William Harris und Richard Brown konnten mit ihren herausragenden Beiträgen überzeugen.", 
        True, 4, 3, 3, "Sport", None),
        
        (9, "Londoner Rugby-Team kämpft sich auf Rang 2 vor", 
        "Das Londoner Rugby-Team hat sich mit einem souveränen 15:6-Sieg gegen Edinburgh auf den zweiten Platz der Liga vorgekämpft. Die Mannschaft zeigt eine starke Form und ist nun bereit, im nächsten Spiel um die Tabellenführung zu kämpfen.", 
        True, 4, 3, 3, "Sport", None),
        
        (10, "Golfspielerin Margaret King holt sich den Titel in London", 
        "Die talentierte Golfspielerin Margaret King hat den prestigeträchtigen Titel in London gewonnen und sich gegen eine starke Konkurrenz durchgesetzt. Mit einem brillanten Spiel sicherte sie sich den ersten Platz und wurde als die beste Spielerin des Turniers gefeiert.", 
        True, 4, 3, 3, "Sport", None),
        
        (11, "Ruderer aus Oxford sichern sich den Sieg im Thames Cup", 
        "Das Ruderteam von Oxford hat den begehrten Thames Cup gewonnen und setzte sich im Finale gegen Cambridge durch. Der dramatische Wettkampf endete mit einer knappen Entscheidung, bei der Oxford knapp vorne lag.", 
        True, 4, 3, 3, "Sport", None),
        
        (12, "Leichtathletik-Wettkampf in Glasgow begeistert Zuschauer", 
        "Der Leichtathletik-Wettkampf in Glasgow war ein voller Erfolg. Zahlreiche neue Rekorde wurden aufgestellt, und die Zuschauer waren begeistert von den athletischen Leistungen, insbesondere im Hürdenlauf und im Stabhochsprung.", 
        True, 4, 3, 3, "Sport", None),
        
        (13, "Londoner Schwimmer glänzen bei internationalen Wettkämpfen", 
        "Die Londoner Schwimmer haben bei den jüngsten internationalen Wettkämpfen großartige Ergebnisse erzielt. Besonders im Freistilschwimmen und Rücken schwammen die Athleten auf dem ersten Platz und holten mehrere Goldmedaillen.", 
        True, 4, 3, 3, "Sport", None),
        
        (14, "Rugby-Duell zwischen Wales und Frankreich endet mit Unentschieden", 
        "Das spannende Rugby-Spiel zwischen Wales und Frankreich endete mit einem gerechten Unentschieden. Beide Teams zeigten starke Leistungen, doch keine Mannschaft konnte sich im Laufe des Spiels einen entscheidenden Vorteil verschaffen.", 
        True, 4, 3, 3, "Sport", None),
        
        (15, "Der 'London Marathon' zieht Tausende von Teilnehmern an", 
        "Der London Marathon lockte auch in diesem Jahr wieder Tausende von Teilnehmern an. Mit einer rekordverdächtigen Anzahl an Läufern aus verschiedenen Teilen der Welt wurde der Wettbewerb zu einem weltweiten Ereignis, das die Stadt in seinen Bann zog.", 
        True, 4, 3, 3, "Sport", None),

        (1, "Squash-Wettkampf in London zieht viele Zuschauer an", 
        "Der kürzlich ausgetragene Squash-Wettkampf in London sorgte für große Begeisterung. Die Spieler zeigten beeindruckende Reflexe und Technik, was den Zuschauern spannende und temporeiche Partien bot. Der Favorit des Turniers, John Davies, sicherte sich den ersten Platz nach einem packenden Finale gegen Charles Manning. Viele Experten sehen in Davies einen zukünftigen Weltmeister, wenn er weiterhin so konstant spielt.", 
        True, 4, 3, 3, "Sport", None),
        
        (2, "Snooker-Meisterschaft in Birmingham endet mit Überraschungssieg", 
        "Die diesjährige Snooker-Meisterschaft in Birmingham ging mit einem überraschenden Sieg von Thomas Reynolds zu Ende. Der unbekannte Spieler setzte sich gegen den amtierenden Champion James Oliver durch und sicherte sich den begehrten Pokal. Seine ruhige und präzise Spielweise beeindruckte sowohl Experten als auch Zuschauer. Viele glauben, dass Reynolds die nächste große Hoffnung des britischen Snookersports ist.", 
        True, 4, 3, 3, "Sport", None),
        
        (3, "Billard-Turnier in Edinburgh: Ein Wettkampf der Präzision", 
        "Das prestigeträchtige Billard-Turnier in Edinburgh zog die besten Spieler des Landes an. Besonders der Kampf um den Titel zwischen den beiden Favoriten, Edward Miller und Richard Palmer, war spannend und forderte die Teilnehmer auf höchstem Niveau. Letztlich setzte sich Miller mit einem überragenden Endspiel durch und wurde als neuer Billardmeister gefeiert. Der Wettbewerb gilt als einer der härtesten im Land und zog zahlreiche Fans und Unterstützer an.", 
        True, 4, 3, 3, "Sport", None),
        
        (4, "Curling-Team aus Schottland gewinnt internationales Turnier", 
        "Das schottische Curling-Team hat kürzlich ein internationales Turnier in Glasgow gewonnen und sich als das beste Team der Saison etabliert. Mit einer außergewöhnlichen Teamarbeit und präzisem Schieben der Steine setzten sie sich gegen die starke Konkurrenz aus Kanada und Schweden durch und holten den begehrten Pokal. Das Team feierte ihren Erfolg mit einer großen Feier, und viele Experten glauben, dass Schottland auch in den kommenden Jahren die Curling-Welt dominieren wird.", 
        True, 4, 3, 3, "Sport", None),
        
        (5, "Polo-Match zwischen London und Oxford sorgt für Aufsehen", 
        "Das Polo-Match zwischen den Teams aus London und Oxford war ein wahrer Höhepunkt des Jahres. Mit schnellen Reitersprüngen und raffinierten Schlägen gaben beide Teams alles. Am Ende setzte sich das Team aus Oxford durch und gewann mit einem knappen 7:6-Sieg, was die Anhänger der Stadt jubeln ließ. Das packende Finale hat viele dazu inspiriert, sich dem Polo-Sport zuzuwenden, und der Sport könnte bald einen neuen Höhepunkt in Großbritannien erreichen.", 
        True, 4, 3, 3, "Sport", None),
        
        (6, "Squash-Klub von Manchester eröffnet neue Trainingsräume", 
        "Der Squash-Klub von Manchester hat seine neuen Trainingsräume eröffnet, die mit modernster Ausstattung und speziellen Wänden für optimale Spielflächen ausgestattet sind. Die Mitglieder freuen sich auf eine verbesserte Trainingsumgebung, die das Niveau des Sports in der Region weiter anheben soll. Mit dieser Erweiterung hofft der Klub, den besten Squash-Spielern des Landes eine erstklassige Trainingsumgebung zu bieten und in den kommenden Jahren erfolgreich an nationalen und internationalen Wettbewerben teilzunehmen.", 
        True, 4, 3, 3, "Sport", None),
        
        (7, "Snooker-Legende James Oliver wird von jungen Talenten herausgefordert", 
        "James Oliver, der unangefochtene Snooker-Champion der letzten Jahre, sieht sich in dieser Saison mit einer neuen Generation von Talenten konfrontiert. Der junge Herausforderer Henry Jenkins hat mit beeindruckenden Siegen in mehreren Turnieren für Aufsehen gesorgt und könnte die alteingesessenen Meister herausfordern. Viele glauben, dass Jenkins Oliver in einem bevorstehenden Duell den Titel streitig machen wird und der Snooker-Sport eine neue Ära erleben könnte.", 
        True, 4, 3, 3, "Sport", None),
        
        (8, "Erstes Billard-Teamturnier in London begeistert die Zuschauer", 
        "Das erste offizielle Billard-Teamturnier in London hat viele Zuschauer angezogen, die die spannende Atmosphäre und die präzise Spieltechnik der Teilnehmer bewunderten. Das Team 'West End' konnte sich im Finale gegen 'East End' durchsetzen und sich als das beste Team der Stadt behaupten. Das Turnier war ein voller Erfolg und wird in den kommenden Jahren sicher zu einer festen Tradition in der Londoner Billard-Szene.", 
        True, 4, 3, 3, "Sport", None),
        
        (9, "Curling: Schottland verteidigt Titel bei den Weltmeisterschaften", 
        "Das schottische Curling-Team hat erneut den Titel bei den Weltmeisterschaften verteidigt. In einem spannenden Endspiel gegen die USA erzielten die Schotten den entscheidenden Punkt und sicherten sich ihren vierten Titel in Folge, was sie zur unbestrittenen Spitzenmannschaft machte. Viele glauben, dass Schottland im internationalen Curling-Sport weiterhin eine dominierende Rolle spielen wird und der Titel auch in den nächsten Jahren in Edinburgh verbleiben könnte.", 
        True, 4, 3, 3, "Sport", None),
        
        (10, "Polo-Wettkampf in Windsor begeistert die Elite", 
        "Das jährliche Polo-Wettkampf in Windsor zog die britische Elite an, darunter viele hochrangige Persönlichkeiten und Adelige. In einem spannenden Finale zwischen den Teams 'Royal Guards' und 'Windsor Knights' siegten die Royal Guards mit einem knappen 5:4 und wurden als neue Champions gefeiert. Der Wettbewerb hat die Bedeutung des Polosports in Großbritannien weiter gestärkt und den Teams neuen Ruhm und Ansehen verschafft.", 
        True, 4, 3, 3, "Sport", None),
        
        (11, "Squash-Meisterschaft in Liverpool von Londoner Spieler gewonnen", 
        "Die diesjährige Squash-Meisterschaft in Liverpool wurde von dem Londoner Spieler Henry Clark gewonnen, der sich mit einer brillanten Leistung gegen die besten Spieler des Landes durchsetzte. Clark zeigte dabei nicht nur beeindruckende Ausdauer, sondern auch eine meisterhafte Technik. Viele glauben, dass Clark der nächste große Star im internationalen Squash werden könnte, wenn er sein Können weiterhin so konstant unter Beweis stellt.", 
        True, 4, 3, 3, "Sport", None),
        
        (12, "Snooker-Weltmeisterschaft in London: Der neue Champion", 
        "Die Snooker-Weltmeisterschaft in London fand mit einem überraschenden Sieg von Albert Green ihren Höhepunkt. Green besiegte in einem spannenden Finale den erfahrenen Spieler Jonathan Grey und sicherte sich den Titel des Weltmeisters. Seine außergewöhnliche Technik und Konzentration brachten ihm den verdienten Erfolg, und er gilt nun als aufstrebender Star der internationalen Snooker-Szene.", 
        True, 4, 3, 3, "Sport", None),
        
        (13, "Billardturnier in Liverpool: Ein spannendes Kopf-an-Kopf-Rennen", 
        "In Liverpool fand ein spannendes Billardturnier statt, das viele Fans in den Bann zog. In einem packenden Kopf-an-Kopf-Rennen zwischen Edward Harding und Thomas Brooks zeigte Brooks hervorragende Technik und sicherte sich den ersten Platz in einem dramatischen Finale. Das Turnier wurde von den Zuschauern begeistert aufgenommen und es wird erwartet, dass auch im nächsten Jahr wieder viele talentierte Spieler daran teilnehmen werden.", 
        True, 4, 3, 3, "Sport", None),
        
        (14, "Curling-Team aus Norwegen gewinnt internationalen Cup", 
        "Das norwegische Curling-Team hat bei den internationalen Curling-Meisterschaften in Glasgow den begehrten Cup gewonnen. Ihre präzise und strategische Spielweise brachte sie am Ende zum verdienten Sieg. Norwegen hat damit seinen Ruf als eines der besten Curling-Teams der Welt weiter gefestigt und wird auch in der kommenden Saison als Topfavorit gehandelt.", 
        True, 4, 3, 3, "Sport", None),
        
        (15, "Polo-Team aus Argentinien setzt sich im internationalen Turnier durch", 
        "Das argentinische Polo-Team hat das internationale Turnier in London gewonnen und setzte sich dabei gegen die britischen Spitzenmannschaften durch. Die Spieler aus Argentinien beeindruckten mit ihrer meisterhaften Kontrolle über das Pferd und die Spieltaktik. Dieser Sieg hat das argentinische Polo-Team als eines der führenden Teams weltweit etabliert.", 
        True, 4, 3, 3, "Sport", None)
    ]

        
    df = pd.DataFrame(newspaper, columns=columns)
    
    # Zufällige Datumswerte zu den fehlenden Einträgen einfügen
    df["spezial_date"] = df["spezial_date"].apply(lambda x: x if pd.notna(x) and x.strip() else generate_random_date())

    
    # Überprüfen auf doppelte IDs und die doppelten auf "unbelegt" setzen
    df["newspaper_event_id"] = df.groupby("newspaper_event_id")["newspaper_event_id"].transform(lambda x: [-1 if i > 0 else val for i, val in enumerate(x)])
    
    return df

def generate_random_date():
    day = random.randint(1, 28)
    month = random.randint(1, 12)
    # Formatierung sicherstellen: "Tag.Monat" (z.B. "25.12")
    return f"{day:02d}.{month:02d}"

# Funktion zur Umwandlung von 'Tag.Monat' in ein Datum
def parse_date(date_str):
    return datetime.strptime(date_str, "%d.%m")

# CSV speichern
def save_to_csv(df, filename="discord_bot/newspaper.csv"):
    df.to_csv(filename, index=False, encoding="utf-8")
    print(f"CSV-Datei '{filename}' erfolgreich erstellt!")
    
# Hauptprogramm
if __name__ == "__main__":
    df = creat_dataframe()
    df['spezial_date'] = df['spezial_date'].apply(lambda x: 
    f"{int(x.split('.')[0]):02d}.{int(x.split('.')[1]):02d}")
    df['spezial_date'] = df['spezial_date'].astype(str)
    save_to_csv(df)
    print(df)