
def run(args):
    inFile,out_dir,config=args
    #
    outFile=os.path.join(out_dir,os.path.basename(inFile))
    outFile=[outFile]


    inFile=[inFile]

    #
    print(outFile,inFile)
    label_operater = HTSLabelNormalisation(question_file_name=config['qs_file_name'], add_frame_features=False,
                                           subphone_feats='none')
    data = label_operater.perform_normalisation(inFile, outFile, label_type=config['label_type'])
    # features, frames_num = BinaryIOCollection().load_binary_file_frame(outFile,label_operater.dimension)
    # print(" {} : features shape {} ".format(os.path.basename(inFile),features.shape))

def build_arg_parser():

    parser=argparse.ArgumentParser(description='parse')
    parser.add_argument('file_id_list',type=str,help='input folder ')
    parser.add_argument('output_dir',type=str,help='input folder ')
    # parser.add_argument('qs_file_name',type=str,default='/mnt/mydrive/home/aghilas/Workspace/Experiments/SynPaFlex-Code/VoiceConversion/cvc-via-ppg/data_fr/misc_question/questions-french_pau-v0.hed',help='input folder ')
    # parser.add_argument('label_type',type=str,default='phone_align',help='input folder ')
