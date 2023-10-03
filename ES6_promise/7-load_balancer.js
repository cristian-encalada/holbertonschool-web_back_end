function loadBalancer(chinaDownload, USDownload) {
  // Race two promises to determine which one resolves first
  return Promise.race([chinaDownload, USDownload]);
}

export default loadBalancer;
