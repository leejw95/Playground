

class USER:

    def __init__(self, tech=None):
        """
        :Function: Set user information and directory paths
        :param tech: (optional) Write your technology to specify directory paths.
                      ex) '028nm' or '065nm' or empty(default: 028nm)
        """
        self.ID = 'yourID'
        self.PW = 'yourPassword'
        self.server = '141.223.22.156'

        # Working Directory
        if tech in ('028nm', None):
            self.Dir_Work = '/mnt/sdc/isjang/OPUS/CAD_S28nm_Workspace'
        elif tech == '065nm':
            self.Dir_Work = '/mnt/sdc/isjang/OPUS/tsmc65'
        else:
            raise NotImplemented

        self.Dir_GDS = self.Dir_Work + '/Download_GDS'      # where the GDS files are uploaded.
        self.Dir_DRCrun = self.Dir_Work + '/DRC/DRC_run'    # Not Used Currently
