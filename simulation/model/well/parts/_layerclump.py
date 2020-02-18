from simulation.common.keywords import Keywords as kw
from simulation.common.words import Words as wrd

class _Layerclump:
    @staticmethod
    def default(agr, well_name, layerclump):
        for idx, layer in enumerate(layerclump):
            name = "'{}_Z{}'".format(well_name.strip("'"),idx+1)
            agr.add_two(kw.layerclump(), name)
            agr.add_three(well_name, ' '.join(layer), kw.mt())
            agr.add_three(well_name, ' '.join(layer), kw.fr())
