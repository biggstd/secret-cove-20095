"""
#################
IDREAM Ontologies
#################

Contains all the ontology definitions used in the IDREAM
database project.
"""


from isatools.model import (
    # Comment,
    # Investigation,
    # OntologySource,
    Characteristic,
    Source,
    OntologyAnnotation,
)


DATA_TYPES = dict(
    simulation=dict(
        name='simulation', type=OntologyAnnotation(term='Simulation'),
        short_display='Simulated', long_display='Simulated Data'
    ),
    experimental=dict(
        name='experimental', type=OntologyAnnotation(term='Experimental'),
        short_display='Experimental', long_display='Experimental Data'
    ),
    literature=dict(
        name='literature', type=OntologyAnnotation(term='Literature'),
        short_display='Literature', long_display='Literature Data'
    ),
)


ONTOLOGY_ANNOTATIONS = dict(
    nmr=dict(
        name='nmr', type=OntologyAnnotation(term='NMR'),
        short_display='NMR', long_display='Nuclear Magnetic Resonance'
    ),
    al27=dict(
        name='al27', type=OntologyAnnotation(term='27 Al'),
        short_display='27 Al', long_display='27 Aluminum'
    ),
)


UNIT_FACTORS = dict(
    molarity=dict(
        name='molarity', type=OntologyAnnotation(term='Molarity'),
        short_display='M', long_display='Molarity'
    ),
    wt_purity=dict(
        name='wt_purity',
        type=OntologyAnnotation(term='Percent Purity by Weight'),
        short_display=u'wt %', long_display='Percent Purity by Weight'
    ),
    celsius=dict(
        name='celsius', type=OntologyAnnotation(term='Celsius'),
        short_display='C', long_display='Degrees Celsius'
    ),
)


FACTOR_FACTORS = dict(
    counter_ion=dict(
        name='counter_ion', type=OntologyAnnotation(term='Counter Ion'),
        short_display='M+', long_display='Counter Ion',
        factor_options=['Na+', 'Li+', 'Cs+', 'K+']
    ),
    data_quality=dict(
        name='data_quality', type=OntologyAnnotation(term='Data quality'),
        short_display='Data Quality', long_display='Data Quality',
        factor_options=['Low', 'Medium', 'High']
    ),
)

MATERIAL_SOURCES = dict(
    al_wire=dict(
        name='Al wire',
        type=Source(
            name='Aluminum Wire',
        )
    ),
    sodium_hydroxide_solid=dict(
        name='Solid Sodium Hydroxide',
        type=Source(
            name='Solid Sodium Hydroxide',
        )
    ),
    potassium_hydroxide_solid=dict(
        name='Solid Potassium Hydroxide',
        type=Source(
            name='Solid Potassium Hydroxide',
        )
    ),
    caesium_hydroxide_solid=dict(
        name='Solid Caesium Hydroxide',
        type=Source(
            name='Solid Caesium Hydroxide',
        )
    ),
    lithium_hydroxide_solid=dict(
        name='Solid Lithium Hydroxide',
        type=Source(
            name='Solid Lithium Hydroxide',
        )
    ),
)


# OntologyAnnotation(term='Percent Purity by Weight'),
# OntologyAnnotation(term='Celsius'),
# OntologyAnnotation(term='NMR Reference Compound'),
# OntologyAnnotation(term='Hydroxide'),
# OntologyAnnotation(term='Aluminum'),
# OntologyAnnotation(term='Sodium'),
# OntologyAnnotation(term='Caesium'),
# OntologyAnnotation(term='Lithium'),
# OntologyAnnotation(term='Potassium'),
